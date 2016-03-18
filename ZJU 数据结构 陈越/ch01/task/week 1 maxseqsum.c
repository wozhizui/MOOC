// 01-复杂度1 最大子列和问题   (20分)
// 给定K个整数组成的序列{ N1, N2,..., N​K}，“连续子列”被定义为
// { Ni,Ni+1,..., Nj}，其中 1<=i<=j<=K。“最大子列和”则被定义为所有连续子列元素的和中最大者。
// 例如给定序列{ -2, 11, -4, 13, -5, -2 }，其连续子列{ 11, -4, 13 }有最大的和20。
// 现要求你编写程序，计算给定整数序列的最大子列和。

// 本题旨在测试各种不同的算法在各种数据情况下的表现。各组测试数据特点如下：

// 数据1：与样例等价，测试基本正确性；
// 数据2：102个随机整数；
// 数据3：103个随机整数；
// 数据4：104个随机整数；
// 数据5：105个随机整数；
// 输入格式:

// 输入第1行给出正整数K≤100000；第2行给出KK个整数，其间以空格分隔。

// 输出格式:

// 在一行中输出最大子列和。如果序列中所有整数皆为负数，则输出0。

// 输入样例:

// 6
// -2 11 -4 13 -5 -2
// 输出样例:

// 20
#include "stdio.h"

int MaxSubseqSum(int seq[], int k);

int main()
{
	int k;
	scanf("%d", &k);
	int seq[k];
	for (int i = 0; i < k; ++i)
	{
		scanf("%d", &seq[i]);
	}
	printf("%d", MaxSubseqSum(seq, k));
	return 0;
}

int MaxSubseqSum(int seq[], int k)
{
	int thissum, maxsum;
	thissum = maxsum = 0;
	for (int i = 0; i < k; ++i)
	{
		thissum += seq[i];
		if (thissum > maxsum)
		{
			maxsum = thissum;
		}
		else if (thissum < 0)
		{
			thissum = 0;
		}
	}
	return maxsum;
}