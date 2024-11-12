- 添加 Q_OBJECT以后编译错误
- Severity	Code	Description	Project	File	Line	Suppression State
Error	LNK2001	unresolved external symbol "public: static struct QMetaObject const IFCentrifugeService::staticMetaObject" (?staticMetaObject@IFCentrifugeService@@2UQMetaObject@@B)	HGTCentrifugeService	D:\Git_Working\E015Basic\E015\Sln_EquipmentService\HGTCentrifugeService\moc_HGTCentrifugeService.obj	1	
- 原因是因为：
- 接口文件也带宏定义 Q_OBJECT关键字
- 接口文件 例如 IFCentrifugeService 也需要单独生成moc文件，添加到工程 之中