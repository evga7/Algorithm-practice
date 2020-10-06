#include <string>
#include <vector>

using namespace std;
int solution(vector<string> lines) {
	int answer = 0;
	int h, m;
	double s,ms;
	int i,j;
	int len = lines.size();
	vector<pair<double,double>>times;
	for (i = 0; i < len; i++)
	{
		h = stoi(lines[i].substr(11, 2))*3600;
		m = stoi(lines[i].substr(14, 2))*60;
		s= stod(lines[i].substr(17, 6));
		ms = stod(lines[i].substr(24, lines[i].size() - 2));
		times.push_back({h + m + s - ms + 0.001, h + m + s });
	}
	//sort(times.begin(), times.end());
	for (i = 0; i < len; i++)
	{
		int cnt = 0;
		double end = times[i].second + 1;
		for (j = i; j < len; j++)
		{
			if (times[j].first<end)
				cnt++;
		}
		answer = max(answer, cnt);
	}
	return answer;
}