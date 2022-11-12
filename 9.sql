select salary from employees join (select DEPARTMENT_ID as id from departments where DEPARTMENT_NAME like '%IT%') as d on d.id=employees.DEPARTMENT_ID GROUP BY salary 
