I=imread('E:/u/sem1/cv/aat1/asignment1/image13.jpg')
imshow(I)
[x,y]=ginput(2)

z=1412.6;
fy=1422.4;
fx=1489.0;
x1=z*(x(1)/fx);
x2=z*(x(2)/fx);
y1=z*(y(1)/fy);
y2=z*(y(2)/fy);
dist=sqrt((y2-y1)^2+(x2-x1)^2);
fprintf('The distqance is %.02f mm',dist);
