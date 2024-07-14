#!/usr/bin/env python3

# * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# * POSSIBILITY OF SUCH DAMAGE.

import networkx as nx
import numpy as np
import argparse
import os
import subprocess
import sys

control_instructions_list = ['jmp', 'jz', 'jne', 'jg', 'jge', 'je', 'jl', 'jn', 'jnz', 'jnb', 'jb', 'jbe', 'ja', 'call']

def get_label_block_map(filename):
  label_map = {}

  with open(filename, 'r') as file:
    current_id = 0

    for line in file:
      label = line.split('\t')[0]
      label = label[:-1]
      label_map[label] = current_id
      
      is_control_transfer = any(substring in line for substring in control_instructions_list)

      if is_control_transfer:
        current_id += 1

  return label_map, current_id


def construct_cfg(dest_path, src_path, input_option, output_option):
  # maintain a map of jump target labels and their block index
  # dictionary with labels as targets, and block index as value
  target_map, size = get_label_block_map(src_path)
  CFG = np.zeros([size, size])

  with open(src_path, 'r') as file:
    for line in file:
      is_control_transfer = any(substring in line for substring in control_instructions_list)

      if is_control_transfer:
        if 'stub' in line:
          # print('stub')
          pass
        elif 'qword' in line:
          # print('qword')
          pass
        else:
          label = line.split('\t')[0]
          label = label[:-1]

          # get jump target label
          target = line.split('\t')[2]
          target = target[2:11]

          # get the current block index
          current_index = target_map[label]

          # was the jump target an address?
          if len(target) < 8:
            target_index = 0
          else:
            target_index = target_map[target]

          CFG[current_index][target_index] = 1

  if output_option == 1:
    # output adjacency list
    cfg_graph = nx.from_numpy_array(CFG, create_using=nx.MultiDiGraph)
    nx.write_adjlist(cfg_graph, dest_path)
  elif output_option == 2:
    # output CSV of adjacency matrix
    np.savetxt(dest_path, CFG, delimiter=",")
  elif output_option == 3:
    # output WL hash value
    cfg_graph = nx.from_numpy_array(CFG, create_using=nx.MultiDiGraph)
    cfg_hash = nx.weisfeiler_lehman_graph_hash(cfg_graph)
    print(cfg_hash)


def decompile_binary(binary_path):
  filename = os.path.basename(binary_path)
  temp_path = "/tmp/cfg/asm/" + filename

  with open(temp_path, "w") as myfile:
    ps1 = subprocess.Popen(["objdump", "-D", "--no-show-raw-insn", "--x86-asm-syntax=intel", binary_path], stdout=myfile, stderr=subprocess.DEVNULL)
    output, error = ps1.communicate()

  return temp_path


if __name__ == "__main__":
  src_path = ""
  dest_path = ""

  parser = argparse.ArgumentParser(description='Control flow graph recovery tool.', usage='cfg <source_file> <dest_file> [<args>]')
  parser.add_argument('src_file', nargs='?', help=argparse.SUPPRESS)
  parser.add_argument('dest_file', nargs='?', help=argparse.SUPPRESS)
  parser.add_argument('--asm', dest='source_file', help='Expects assembly input')
  parser.add_argument('--bin', dest='bin_file', help='Expects binary file as input')
  parser.add_argument('--list', dest='list_file', help='Outputs CFG in adjacency list format')
  parser.add_argument('--matrix', dest='csv_file', help='Outputs CFG as an adjacency matrix in CSV format')
  parser.add_argument('--hash', dest='hash', action='store_true', help='Outputs a hash value representing the graph\'s isomorphism using Weisfeiler-Lehman graph hashing')
  
  # sorry, this is a hack
  input_option = 1
  output_option = 1

  args = parser.parse_args()
  
  if len(sys.argv) == 1:
    parser.print_help()
    print("\nauthor: John Musgrave <@musgravejw>, 2019-2022.\n")
  else:
    if args.source_file:
        input_option = 1
        src_path = args.source_file
    elif args.bin_file:
        input_option = 2
        src_path = decompile_binary(args.bin_file)
    else:
        input_option = 1
        src_path = args.src_file

    if args.list_file:
        output_option = 1
        dest_path = args.list_file
    elif args.csv_file:
        output_option = 2
        dest_path = args.csv_file
    elif args.hash:
        output_option = 3
        dest_path = ""
    else:
        output_option = 1
        dest_path = args.dest_file

    construct_cfg(dest_path, src_path, input_option, output_option)
