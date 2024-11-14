- String Hex To Int Value
```
// example 0x32 -> 50
uint32_t  hex_to_integer(const  std::string&  inputString)
{
	const  char  *s  =  inputString.c_str();
	if (!s  ||  !*s)
		return  0;
	uint32_t  num  =  0;
	char  c  =  0;
	if (sscanf(s, "%x%c", &num, &c) ==  1)
		return  num;
	else
		return  0;
}
```