```
std::string LaserControl::charToHexString(unsigned char* bytes, int len)
{
	const char HEX[] = "0123456789ABCDEF";
	std::string lStr;
	for (int i = 0; i < len; i++)
	{
		char lTemp = bytes[i];
		lStr.push_back(HEX[(lTemp & 0xf0) >> 4]);
		lStr.push_back(HEX[lTemp & 0x0f]);
		if (i < len - 1)
		{
			lStr += " ";
		}
	}
	return lStr;
}
```