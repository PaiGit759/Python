let s = ''
let  a = [5, 8 , 9, 0, 66, 18]

for (i=1; i < length(a); i++ ) {

if (isEven(a[i]) && a[i-1]%3==0)    
{    s += a[i] / 2
}
else {
    s += a[i] * 2
}
}
console.log(s)
