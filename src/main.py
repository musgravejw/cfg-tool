import networkx as nx
import numpy as np

control_instructions_list = ['jmp', 'jz', 'jne', 'jg', 'jge', 'je', 'jl', 'jn', 'jl', 'jnz', 'jnb', 'jz', 'jb', 'jbe', 'ja', 'call']

def get_label_block_map(filename):
  map = {}

  with open(filename, 'r') as file:
    current_id = 0

    for line in file:
      label = line.split('\t')[0]
      label = label[:-1]
      map[label] = current_id
      
      is_control_transfer = any(substring in line for substring in control_instructions_list)

      if is_control_transfer:
        current_id += 1

  return map, current_id


with open(src_file, 'r') as file:
  DDG = np.zeros([DDG_SIZE, DDG_SIZE])
  operand_index_dictionary = {}

  for line in file:
    is_control_transfer = any(substring in line for substring in control_instructions_list)

    if is_control_transfer:
      if 'stub' in line:
        print('stub')
      elif 'qword' in line:
        print('qword')
      else:
        print(line)

        label = line.split('\t')[0]
        label = label[:-1]

        # get jump target label
        target = line.split('\t')[2]
        target = target[2:11]

        # get the current block index
        current_index = target_map[label]

        # was the jump target a register?
        if len(target) < 8:
          target_index = 0
        else:
          target_index = target_map[target]

        # you don't need the CFG if you have the PDG
        # should add an option to output the graph
        # CFG.add_edge(current_index, target_index)
        # CFG[current_index][target_index] = 1
        # CFG[target_index][current_index] = 1


        ddg_graph = nx.from_numpy_array(DDG)
        ddg_graph.remove_nodes_from(list(nx.isolates(ddg_graph)))

        # add DDG graph to PDG tensor
        # let's start with an undirected CFG

        ddg_hash = nx.weisfeiler_lehman_graph_hash(ddg_graph)

        # real_value
        real = hash_to_real(ddg_hash)

        PDG[current_index][target_index] = real
        PDG[target_index][current_index] = real

      # reset the DDG
      DDG = np.zeros([DDG_SIZE, DDG_SIZE])
      operand_index_dictionary = {}

    else:
      # extract DDG from block
      items = line.split("mov")

      if (len(items) > 1):
        operands = items[1].split(",")

        if (len(operands) > 1):
          dest = get_index_for_operand(operands[0].strip(), operand_index_dictionary)
          source = get_index_for_operand(operands[1].strip(), operand_index_dictionary)

          # this is undirected, could do directed, and then compare graph composition
          DDG[dest][source] = 1
          DDG[source][dest] = 1
        else:
          print(operands)
