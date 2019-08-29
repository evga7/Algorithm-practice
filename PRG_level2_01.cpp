string solution(int n) {
	string answer = "";
	int temp;
	while (n > 0)
	{
		temp = n % 3;
		n /= 3;
		if (temp == 0)
		{
			temp = 4;
			n--;
		}
		answer = to_string(temp) + answer;
	}
	return answer;
}