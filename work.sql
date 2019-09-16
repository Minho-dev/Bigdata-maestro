select * 
from emp
where sal > (select sal from emp where ename = 'JONES' )

select *
from emp
where comm > (select comm from emp where ename = 'ALLEN' )

select *
from emp
where hiredate < (select hiredate from emp where ename = 'SCOTT' )

select e.empno, e.ename, e.job, e.sal, d.deptno, d.dname, d.loc
from emp e, dept d
where e.deptno = d.deptno
and e.deptno = 20
and e.sal > ( select avg( sal ) from emp )

select e.empno, e.ename, e.job, e.sal, d.deptno, d.dname, d.loc
from emp e, dept d
where e.deptno = d.deptno
and e.deptno = 20
and sal <= (select avg(sal) from emp)

select *
from emp
where deptno in (20, 30)

select *
from emp
where sal in (select max(sal) from emp group by deptno )

select *
from emp
where sal = any (select max(sal) from emp group by deptno )

select *
from emp
where sal < any ( select sal from emp where deptno = 30 )
order by sal, empno

select *
from emp
where sal > any (select sal from emp where deptno = 30 )

select * 
from emp
where hiredate < all (select hiredate from emp where deptno = 10 )

select *
from emp
where ( deptno, sal ) in (select deptno, max(sal) from emp group by deptno )

select e.empno, e.ename, e.deptno, d.dname, d.loc
from (select * from emp where deptno = 10) e, (select * from dept) d
where e.deptno = d.deptno

with
e as (select * from emp where deptno = 10 ),
d as (select * from dept)
select e.empno, e.ename, e.deptno, d.dname, d.loc
from e, d
where e.deptno = d.deptno

select empno, ename, job, sal, (select grade from salgrade where e.sal between losal and hisal ) as salgrade,
deptno, ( select dname from dept where e.deptno = dept.deptno ) as dname
from emp e;

select e.empno, e.ename, e.job, d.deptno, d.dname, d.loc
from emp e, dept d
where e.deptno = d.deptno
and e.deptno = 10
and job <> all (select job from emp where deptno = 30 )

select e.empno, e.ename, e.job, d.deptno, d.dname, d.loc
from (select * from emp where deptno = 10 ) e, dept d
where e.deptno = d.deptno
and job <> all (select job from emp where deptno = 30 )

select e.empno, e.ename, e.sal, s.grade
from emp e, salgrade s
where sal > (select max(sal) from emp where job = 'SALESMAN' )
and e.sal between s.losal and s.hisal
order by empno

select e.empno, e.ename, e.sal, s.grade
from emp e, salgrade s
where sal > all (select sal from emp where job = 'SALESMAN' )
and e.sal between s.losal and s.hisal
order by empno

create table dept_temp
as select * from dept;
select * from dept_temp;

insert into dept_temp ( deptno, dname, loc ) values ( 50, 'DATABASE', 'SEOUL' );
insert into dept_temp values ( 60, 'NETWORK', 'BUSAN' );
INSERT into dept_temp (deptno, dname, loc ) values ( 70, 'WEB', null );
insert into dept_temp (deptno, dname, loc ) values ( 80, 'MOBILE', '' );
insert into dept_temp (deptno, loc ) values ( 90, 'INCHEON' );

create table emp_temp as select * from emp where 1 <> 1;
select * from emp_temp;
insert into emp_temp ( empno, ename, job, mgr, hiredate, sal, comm, deptno )
values ( 9999, '홍길동', 'PRESIDENT', NULL, '2001/01/01', 5000, 1000, 10 );
insert into emp_temp ( empno, ename, job, mgr, hiredate, sal, comm, deptno )
values ( 1111, '성춘향', 'MANAGER', 9999, '2001-01-05', 4000, null, 20 );
insert into emp_temp ( empno, ename, job, mgr, hiredate, sal, comm, deptno )
values ( 2111, '이순신', 'MANAGER', 9999, to_date( '07/01/2001', 'DD/MM/YYYY' ), 4000, null, 20 );
insert into emp_temp ( empno, ename, job, mgr, hiredate, sal, comm, deptno )
values ( 3111, '심청이', 'MANAGER', 9999, sysdate, 4000, null, 30 );
insert into emp_temp ( empno, ename, job, mgr, hiredate, sal, comm, deptno )
select e.empno, e.ename, e.job, e.mgr, e.hiredate, e.sal, e.comm, e.deptno
from emp e, salgrade s
where e.sal between s.losal and s.hisal
and s.grade = 1;

create table dept_temp2 as select * from dept;
select * from dept_temp2;

drop table _temp;

create table chap10hw_emp as select * from emp;
create table chap10hw_dept as select * from dept;
create table chap10hw_salgrade as select * from salgrade;

insert into chap10hw_dept (deptno, dname, loc ) values (50, 'ORACLE', 'BUSAN');
INSERT INTO CHAP10HW_DEPT VALUES (60, 'SQL', 'ILSAN');
INSERT INTO CHAP10HW_DEPT VALUES (70, 'SELECT', 'INCHEON');
INSERT INTO CHAP10HW_DEPT VALUES (80, 'DML', 'BUNDANG');
SELECT * FROM chap10hw_dept;

SELECT * FROM chap10hw_emp;
INSERT INTO CHAP10HW_EMP VALUES (7201, 'TEST_USER1', 'MANAGER', 7788, '2016-01-02', 4500, NULL, 50 );
INSERT INTO CHAP10HW_EMP VALUES (7202, 'TEST_USER2', 'CLERK', 7201, '2016-02-21', 1800, NULL, 50 );

UPDATE CHAP10HW_EMP
SET DEPTNO = 70
WHERE SAL > (SELECT AVG(SAL) FROM CHAP10HW_EMP WHERE DEPTNO = 50 );

