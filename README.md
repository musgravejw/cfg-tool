# cfg-tool
![GitHub License](https://img.shields.io/github/license/musgravejw/cfg-tool)
![GitHub Tag](https://img.shields.io/github/v/tag/musgravejw/cfg-tool)

This tool recovers the control flow graph from a static binary.  The graph can be exported in multiple formats, either adjacency list, adjacency matrix CSV, or isomorphic hash.

# Citation
To cite this tool, please use the following BibTex citation:
```
@INPROCEEDINGS{10670673,
  author={Musgrave, John and Ralescu, Anca},
  booktitle={NAECON 2024 - IEEE National Aerospace and Electronics Conference}, 
  title={kNN Classification of Malware Data Dependency Graph Features}, 
  year={2024},
  volume={},
  number={},
  pages={206-213},
  keywords={Training;Measurement;Accuracy;Semantics;Aerospace electronics;Feature extraction;Malware;machine learning;feature extraction;malware analysis},
  doi={10.1109/NAECON61878.2024.10670673}}

```

# Install
Run:
```
$ git clone https://github.com/musgravejw/cfg-tool
$ cd ./cfg-tool
$ pip install -r ./requirements.txt
$ sudo make install
```

# Usage
- Install
- Run `cfg [source_file] [dest_file]` 

### `--asm [source_file]`
Assumes assembly input.  This is the default, when unspecified.  Assembly file from `objdump` output is expected with `intel` format specified.  `source_file` parameter is a path to the assembly file.

### `--bin [source_file]`
Expects a binary as input.  This option performs decompilation the binary.  `source_file` is a path to the binary.

### `--list [dest_file]`
Outputs the graph in adjacency list format.  This is the default, when unspecified.  `dest_file` is a path for the output file.

### `--matrix [dest_file]`
Outputs the graph as an adjacency matrix in `csv` format.  This is compatible with NumPy matrices, and NetworkX graphs.  The matrix can be imported by either of these libraries using CSV import.  `dest_file` is a path for the output file.

### `--hash`
Outputs a hash value representing the graph's isomorphism using Weisfeiler-Lehman graph hashing.  Defaults to `STDOUT`.

# Documentation
Please see `/docs/README`.

# License
This project uses the GNU Public License Version 3.  Please see the [LICENSE](https://github.com/musgravejw/cfg-tool/blob/HEAD/LICENSE) for more information.
```
 THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 POSSIBILITY OF SUCH DAMAGE.
```

# Author
John Musgrave <@musgravejw>, 2019-2022.
