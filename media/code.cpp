#include<iostream>
#include<bits/stdc++.h>
#define ll long long
using namespace std;
int main(){
string s;
cin>>s;
ll sum=1,maxi=1;
for(ll i=1;i<s.size();i++){
 if(s[i]==s[i-1]){
     sum++;
    maxi=max(maxi,sum);
 }
 else{
sum=1;
 }
}
cout<<maxi;
    return 0;
}