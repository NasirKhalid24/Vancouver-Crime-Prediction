
m = csvread('crime.csv', 1,10);
x = m(:,1);
y = m(:,2);
x(x == 0) = [];
y(y == 0) = [];

ind1 = find(y<-123.5);
ind2 = (find(y>-122.9));
ind = [ind1;ind2];

x(ind) =[];
y(ind) =[];

a = -0.001;
b = 0.001;
r = (b-a).*rand(1000,1) + a;

r = r(randperm(2))';

pt = m(randperm(size(m,1),1),:);
pt_shited = pt + r;

pt_shifted = pt;


plot(y, x, 'rx')
hold on;
plot(pt_shifted(2),pt_shifted(1), 'yo');
hold on;

plot(-123.13695151,49.28256612, 'bo');