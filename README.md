# burnet
Extract the version of Xcode built from the IPA file.  
Inspired by [here](https://qiita.com/bricklife/items/8b7c9dc4f7ab164e738d).
  
## Python Version
  
```bash
> python -V
Python 3.8.5
```
  
## How to use
  
```bash
> python main.py {IPA_FILE_PATH}
```
  
## Example
  
```bash
> ls
Test20201016.ipa
main.py

> python main.py ./Test20201016.ipa
12A7300  # Xcode12.0.1 (12A7300)
```
  