#include <stdio.h>
void doubles()
{
	int arr[201] = { 0 };
	int arr2[201] = { 0 };
	int N;
	int cnt = 0;
	int i;
	int cnt2 = 0;
	//N�� �Է¹ް� arr[N]��°�� ���� 1�� �Է½��Ѽ�
	//N��°�� ���Դٴ°��� �Է¹ް� arr2�� �� ������ ����
	//�׷��� arr�� �迭�� arr2[]�� *2 ���� 1�̸� �����ΰ����ִ°��̹Ƿ� cnt����
	while (1) 
	{
		scanf("%d", &N);
		if (N == -1)
			break;
		if (N == 0)
		{
			for (i = 0;i < cnt;i++)
			{
				if (arr[arr2[i]*2]==1) 
					cnt2++;
			}
			printf("%d\n", cnt2);
			for (i = 0;i < cnt;i++) //arr �Լ��� �ʱ�ȭ
			{
				arr[arr2[i]] = 0;
				arr2[i] = 0;
			}
			cnt = cnt2 = 0;
		}
		else
		{
			arr2[cnt++] = N;
			arr[N] = 1;
		}

	}
}
int main()
{
	doubles();
}
