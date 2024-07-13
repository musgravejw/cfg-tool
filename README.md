# cfg-tool
![GitHub License](https://img.shields.io/github/license/musgravejw/cfg-tool)
![GitHub Tag](https://img.shields.io/github/v/tag/musgravejw/cfg-tool)

This tool recovers the control flow graph from a static binary.  The graph can be exported in multiple formats, either adjacency list, adjacency matrix, or isomorphic hash.


# Citation
To cite this tool, please use the following BibTex citation:
```
@misc{musgrave2024knnclassificationmalwaredata,
      title={kNN Classification of Malware Data Dependency Graph Features}, 
      author={John Musgrave and Anca Ralescu},
      year={2024},
      eprint={2406.02654},
      archivePrefix={arXiv},
      primaryClass={cs.CR},
      url={https://arxiv.org/abs/2406.02654}, 
}
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
- Run `sem create && cd sem_home` 
- Select binaries to compose the library.  Copy files to `'data'`.
- Run `sem init`.
- Select an example to search for similarity.

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
John Musgrave <@musgravejw>, 2019-2024.
