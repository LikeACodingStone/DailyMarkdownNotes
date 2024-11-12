```
	ofstream outfile;
	outfile.open(filePath, ios::out | ios::trunc);
	if (outfile) {
		float h1 = 0.332;
		float h2 = 5.65746;
		float h3 = -56.2547;
		outfile << setw(7) << setfill('0') << setiosflags(ios::fixed)
				<< setprecision(6) << h1 
				<< ",	" << h2 << ",	" << h3 << endl;

	}
	outfile.close();
```