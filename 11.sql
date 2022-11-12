select * from Customer join (select * from Salesman WHERE city = 'London') as s on s.salesman_id = Customer.salesman_id  WHERE city = 'London';

