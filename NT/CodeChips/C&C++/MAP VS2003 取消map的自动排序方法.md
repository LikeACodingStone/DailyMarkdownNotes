```
struct MyComparator {
	bool operator()(const std::string& lhs, const std::string& rhs) const {
		return false;
	}
};

int main(int argc, char **argv)
{
	std::multimap<std::string, int, MyComparator> myMultimap;
	myMultimap.insert(make_pair("Oppo", 1));
	myMultimap.insert(make_pair("Apple", 2));
	myMultimap.insert(make_pair("Test", 3));
	std::multimap<string, int, MyComparator>::iterator itera;
	for(itera = myMultimap.begin(); itera != myMultimap.end(); itera++)
	{
		string keyVal = itera->first;
		int ccc=0;
	}
}
```