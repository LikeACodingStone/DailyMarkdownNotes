## A14

https://buildbot-sy.nts.neusoft.local/buildbot/#/projects/27

http://naisftp_sy.nts.neusoft.local/CN_Buildbot/buildbot/integration/bosch/ccs20/buildresults/dev/ccs2/ccs2_ccs2_etc_vics_qpr3_a12_dev/tagged/

tag名:
own/release/CCS2_Nissan_2521.1a_int  

#### 1. 根据commit ID 逐个去gerrit 找到cherry-pick 连接，cherry-pick到VF_A14(VF_A12)
#### 2. Squash 所有变更，修改message
#### 3. PUSH
```
git push origin HEAD:refs/for/ccs2_ccs2_etc_vics_a12_vf_int
git push origin HEAD:refs/for/ccs2_ccs2_etc_vics_a14_vf_int
git push origin HEAD:refs/for/ccs2_ccs2_etc_vics_a12_vf_int


smartgit
refs/for/ccs2_ccs2_etc_vics_a12_vf_int
refs/for/ccs2_ccs2_etc_vics_a14_vf_int
```



