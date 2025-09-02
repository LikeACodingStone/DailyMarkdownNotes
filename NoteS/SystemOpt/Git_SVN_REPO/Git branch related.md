# Push To Review
`
git push --porcelain --progress --recurse-submodules=check origin refs/heads/branch_name:refs/for/branch_name
`
***
# Recurse 
 - recurse pull
`
git pull --recurse-submodules 
`
 - recurse checkout
`
git checkout branch_name --recurse-submodules
`
***
# Create Local Branch For Remote Mirror
 - already exists remote
`
  remotes/origin/stabilization/2024/product_vics_CCS2_LGE
`

 - create only 
`
git branch stabilization/2024/product_vics_CCS2_LGE --track   remotes/origin/stabilization/2024/product_vics_CCS2_LGE
`

 - create and checkout
```
git checkout -b stabilization/2024/product_vics_CCS --track   remotes/fred/stabilization/2024/product_vics_CCS2_LGE
```
***
- pull remote, abow example 
```
git pull fred stabilization/2024/product_vics_CCS2_LGE
//will update local branch stabilization/2024/product_vics_CCS
```
