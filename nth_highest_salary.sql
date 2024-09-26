CREATE FUNCTION getNthHighestSalary(n INT) RETURNS INT
BEGIN
  DECLARE nth_highest_salary INT;
  DECLARE offset_value INT;

  -- Return null if n is less than or equal to 0
  IF n <= 0 THEN
    RETURN NULL;
  END IF;

  -- Calculate the offset value as n - 1
  SET offset_value = n - 1;

  -- Fetch the nth highest salary
  SET nth_highest_salary = (
    SELECT salary
    FROM (
      SELECT DISTINCT salary 
      FROM Employee
      ORDER BY salary DESC
    ) AS temp
    LIMIT 1 OFFSET offset_value
  );

  -- Return the nth highest salary or null if it doesn't exist
  RETURN nth_highest_salary;
END;
