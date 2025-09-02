- 查找文件数量
```
find ~ | wc -l
```
- 查找文件数量最多的文件夹
```
find ~ -xdev -type f | cut -d/ -f1-5 | sort | uniq -c | sort -nr | head -20
```