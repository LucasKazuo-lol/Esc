DECLARE
    cont number(3) := 0;
BEGIN
    DBMS_OUTPUT.PUT_LINE('Comeco contador');
    LOOP
        EXIT WHEN cont > 100;
        DBMS_OUTPUT.PUT_LINE('Cont ' || cont);
        IF MOD(cont, 5) = 0 THEN
            DBMS_OUTPUT.PUT_LINE('deu cinco');
        END IF;
        cont := cont + 1;
    END LOOP;
    DBMS_OUTPUT.PUT_LINE('fim');
END;

   
begin
  for i in  1..100
    loop
        if mod(power(i,2),5) = 0 then
            DBMS_OUTPUT.PUT_LINE(power(i,2) || 'é exponencial de 5');
        end if;

    end loop;    
end;


DECLARE
    num NUMBER(3) := 0;
BEGIN
    WHILE num < 60 LOOP
        num := ROUND(DBMS_RANDOM.VALUE(1, 100));
        DBMS_OUTPUT.PUT_LINE(num);
    END LOOP;
END;

--https://onecompiler.com/plsql--