-- SQL-команды для создания таблиц

CREATE TABLE customers_data
	(
		customer_id CHAR(5) PRIMARY KEY,
		company_name CHAR(255),
		contact_name CHAR(50)
	);

CREATE TABLE employees_data
	(
		employee_id SERIAL PRIMARY KEY,
		first_name CHAR(15),
		last_name CHAR(15),
		title CHAR(50), -- здесь конечно же нужен ENUM
		birth_date DATE,
		notes TEXT
	);

CREATE TABLE orders_data
	(
		order_id INT PRIMARY KEY,
		customer_id CHAR(5) REFERENCES customers_data(customer_id),
		employee_id INT REFERENCES employees_data(employee_id),
		order_date DATE,
		ship_city CHAR(20)
	);
