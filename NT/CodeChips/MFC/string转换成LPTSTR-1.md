```
string fileName = CreateTimeFile() + ".data";
std::wstring wstr(fileName.begin(), fileName.end());
LPCWSTR lpwstr = wstr.c_str();
LPTSTR result = (LPTSTR) lpwstr;
```