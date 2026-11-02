
```bash
# ROCm Status, AMD GPU Running Status
watch -n 1 rocm-smi

# both two command are the same function
sysctl vm.max_map_count
#
cat /proc/sys/vm/max_map_count

```

> [! vm.max_map_count]
> `vm.max_map_count` is a Linux kernel parameter that defines the maximum number of virtual memory mapping areas (VMA) a single process can create. SonarQube requires a sufficiently high value because its Elasticsearch search engine uses Lucene to index and search code analysis data, relying on memory-mapped files (`mmap()`) for efficient access to index files. If the limit is too low, Elasticsearch may fail to create the necessary memory mappings, causing indexing or search failures, or even preventing the search engine from starting. Increasing this limit does not directly improve search speed or consume additional RAM; it simply allows Elasticsearch to create enough memory mappings to operate reliably.