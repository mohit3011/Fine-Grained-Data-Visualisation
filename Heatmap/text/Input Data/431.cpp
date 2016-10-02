#include<bits/stdc++.h>
using namespace std;

#define max(a,b) ((a)>(b)?(a):(b))
#define min(a,b) ((a)>(b)?(b):(a))

#define rep(i,a,b) for(i=a;i<b;i++)
#define F first
#define S second
#define pb push_back
#define sqr(a) (a)*(a)
#define Pi 3.141592653589793
#define MOD 1000000007

// For i/o
#define sd1(a) scanf("%d",&a)
#define sd2(a,b) scanf("%d %d",&a,&b)
#define sd3(a,b,c) scanf("%d%d%d",&a,&b,&c)
#define sf scanf
#define pf printf
// For debugging
#define deb(a) printf("deb%d\n",a)

int i,j;
int n,k,d;
int dp[101][2];
/*
int func1(int num)
{
	if(dp[num][0] != -1)
		return dp[num][0];
	else
	{
		int temp = 0;
		int t = num-1;
		while(t >= 0)
		{
			temp = (temp%MOD + func1(t))%MOD;
			t -= 1;
		}
		dp[num][0] = temp%MOD;
		return dp[num][0];
	}
}

int func2(int num)
{
	deb(0);
	if(dp[num][1] != -1)
		return dp[num][1];
	else if(num < d)
		return 0;
	else
	{
		int temp = 0;
		int t = num-1;
		while(t >= n - min(n,d-1))
		{
			temp = (temp%MOD + func2(t))%MOD;
			t -= 1;
		}
		t = n-d;
		while(t >= n - min(n,k));
		{
			temp = (temp%MOD + (func2(t) + func1(t))%MOD)%MOD;
			t -= 1;
		}
		dp[num][1] = temp;
		return dp[num][1];
	}
}
*/
int main()
{
	sd3(n,k,d);
	rep(i,0,101)
	{
		dp[i][0] = 0;
		dp[i][1] = 0;
	}
	dp[0][0] = 1;
	dp[0][1] = 0;
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=k;j++)
		{
			if(i-j < 0)
				break;
			if(j < d)
			{
				dp[i][0] = (dp[i][0] + dp[i-j][0])%MOD;
				dp[i][1] = (dp[i][1] + dp[i-j][1])%MOD;
			}
			else
			{
				dp[i][1] = (dp[i][1] + dp[i-j][0])%MOD;
				dp[i][1] = (dp[i][1] + dp[i-j][1])%MOD;
			}
		}
	}
	pf("%d\n",dp[n][1]);
	return 0;
}
