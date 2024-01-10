i = 1;

def sqlQuery(queryNumber, *values):
    if queryNumber == 1:
        query = f"""
            SELECT
            F1.DISPLAY AS NAME,
            F1.BIRTHDAY,
            F1.EMAIL,
            DATEDIFF(YEAR, CONVERT(DATE, F1.BIRTHDAY, 103), GETDATE()) AS YAS,
            CASE
                WHEN CAST(DATEDIFF(DAY, GETDATE(), DATEADD(YEAR, DATEDIFF(YEAR, CONVERT(DATE, F1.BIRTHDAY, 103), GETDATE()), CONVERT(DATE, F1.BIRTHDAY, 103))) AS VARCHAR(MAX)) = '0'
                THEN 'BUGÜN DOĞUM GÜNÜ'
                ELSE CAST(DATEDIFF(DAY, GETDATE(), DATEADD(YEAR, DATEDIFF(YEAR, CONVERT(DATE, F1.BIRTHDAY, 103), GETDATE()), CONVERT(DATE, F1.BIRTHDAY, 103))) AS VARCHAR(MAX))
            END AS KACGUNKALDI,
            ISNULL(CAST(F3.BASE64FILE1 AS VARCHAR(MAX)), '') AS BASE64FILE1, ISNULL(CAST(F3.BASE64FILE2 AS VARCHAR(MAX)), '') AS BASE64FILE2,
            ISNULL(CAST(F3.BASE64FILE3 AS VARCHAR(MAX)), '') AS BASE64FILE3, ISNULL(CAST(F3.BASE64FILE4 AS VARCHAR(MAX)), '') AS BASE64FILE4,
            ISNULL(CAST(F3.BASE64FILE5 AS VARCHAR(MAX)), '') AS BASE64FILE5, ISNULL(CAST(F3.BASE64FILE6 AS VARCHAR(MAX)), '') AS BASE64FILE6,
            ISNULL(CAST(F3.BASE64FILE7 AS VARCHAR(MAX)), '') AS BASE64FILE7, ISNULL(CAST(F3.BASE64FILE8 AS VARCHAR(MAX)), '') AS BASE64FILE8,
            ISNULL(CAST(F3.BASE64FILE9 AS VARCHAR(MAX)), '') AS BASE64FILE9, ISNULL(CAST(F3.BASE64FILE10 AS VARCHAR(MAX)), '') AS BASE64FILE10,
            ISNULL(CAST(F3.BASE64FILE11 AS VARCHAR(MAX)), '') AS BASE64FILE11, ISNULL(CAST(F3.BASE64FILE12 AS VARCHAR(MAX)), '') AS BASE64FILE12,
            ISNULL(CAST(F3.BASE64FILE13 AS VARCHAR(MAX)), '') AS BASE64FILE13, ISNULL(CAST(F3.BASE64FILE14 AS VARCHAR(MAX)), '') AS BASE64FILE14,
            ISNULL(CAST(F3.BASE64FILE15 AS VARCHAR(MAX)), '') AS BASE64FILE15, ISNULL(CAST(F3.BASE64FILE16 AS VARCHAR(MAX)), '') AS BASE64FILE16,
            ISNULL(CAST(F3.BASE64FILE17 AS VARCHAR(MAX)), '') AS BASE64FILE17, ISNULL(CAST(F3.BASE64FILE18 AS VARCHAR(MAX)), '') AS BASE64FILE18,
            ISNULL(CAST(F3.BASE64FILE19 AS VARCHAR(MAX)), '') AS BASE64FILE19, ISNULL(CAST(F3.BASE64FILE20 AS VARCHAR(MAX)), '') AS BASE64FILE20,
            ISNULL(CAST(F3.BASE64FILE21 AS VARCHAR(MAX)), '') AS BASE64FILE21, ISNULL(CAST(F3.BASE64FILE22 AS VARCHAR(MAX)), '') AS BASE64FILE22,
            ISNULL(CAST(F3.BASE64FILE23 AS VARCHAR(MAX)), '') AS BASE64FILE23, ISNULL(CAST(F3.BASE64FILE24 AS VARCHAR(MAX)), '') AS BASE64FILE24,
            ISNULL(CAST(F3.BASE64FILE25 AS VARCHAR(MAX)), '') AS BASE64FILE25, ISNULL(CAST(F3.BASE64FILE26 AS VARCHAR(MAX)), '') AS BASE64FILE26,
            ISNULL(CAST(F3.BASE64FILE27 AS VARCHAR(MAX)), '') AS BASE64FILE27, ISNULL(CAST(F3.BASE64FILE28 AS VARCHAR(MAX)), '') AS BASE64FILE28,
            ISNULL(CAST(F3.BASE64FILE29 AS VARCHAR(MAX)), '') AS BASE64FILE29, ISNULL(CAST(F3.BASE64FILE30 AS VARCHAR(MAX)), '') AS BASE64FILE30
        FROM
            IASADRBOOKCONTACT F1
        INNER JOIN
            IASHCMPER F2 ON F2.CLIENT = F1.CLIENT AND F2.CONTACTNUM = F1.CONTACTNUM AND F2.EMPLTYPE = 0 AND F2.ISDELETED = 0
        LEFT OUTER JOIN 
            TABLE2 F3 ON F3.CLIENT = F1.CLIENT AND F3.EMPLOYEE = F1.DISPLAY
        WHERE
            F1.CLIENT = '00'
            AND F1.ISDELETED = 0
            AND F1.CISCUSTORVEND = 0
            AND DATEDIFF(DAY, GETDATE(), DATEADD(YEAR, DATEDIFF(YEAR, CONVERT(DATE, F1.BIRTHDAY, 103), GETDATE()), CONVERT(DATE, F1.BIRTHDAY, 103))) BETWEEN 0 AND 15
            AND F1.BIRTHDAY <> ''
        ORDER BY CAST(CAST(DATEDIFF(DAY, GETDATE(), DATEADD(YEAR, DATEDIFF(YEAR, CONVERT(DATE, F1.BIRTHDAY, 103), GETDATE()), CONVERT(DATE, F1.BIRTHDAY, 103))) AS VARCHAR(MAX)) AS INT)
        """


    elif queryNumber == 2:
        query = f"""
            SELECT '0x' + UPPER(PASSW)
            FROM IASUSERS
            WHERE CLIENT = '00' AND ISBLOCKED = 0 AND USERNAME = '{values[0]}' AND PASSW = '{values[1]}'
        """


    elif queryNumber == 3:
        query = f"""
            INSERT INTO TABLE4 VALUES (
                {chr(39)}00{chr(39)},
                {chr(39)}{values[0]}{chr(39)},
                0,
                {chr(39)}{values[1]}{chr(39)},
                GETDATE(),
                {chr(39)}{values[1]}{chr(39)},
                GETDATE(),
                {chr(39)}{values[2]}{chr(39)},
                {chr(39)}{values[3]}{chr(39)},
                {chr(39)}{values[4]}{chr(39)},
                {chr(39)}{values[5]}{chr(39)},
                {chr(39)}{values[6]}{chr(39)},
                {chr(39)}{values[7]}{chr(39)},
                {chr(39)}{values[8]}{chr(39)},
                {chr(39)}{values[9]}{chr(39)},
                {chr(39)}{values[10]}{chr(39)},
                {chr(39)}{values[11]}{chr(39)},
                {chr(39)}{values[12]}{chr(39)},
                {chr(39)}{values[13]}{chr(39)},
                {chr(39)}{values[14]}{chr(39)},
                {chr(39)}{values[15]}{chr(39)},
                {chr(39)}{values[16]}{chr(39)},
                {chr(39)}{values[17]}{chr(39)},
                {chr(39)}{values[18]}{chr(39)},
                {chr(39)}{values[19]}{chr(39)},
                {chr(39)}{values[20]}{chr(39)},
                {chr(39)}{values[21]}{chr(39)},
                {chr(39)}{values[22]}{chr(39)},
                {chr(39)}{values[23]}{chr(39)},
                {chr(39)}{values[24]}{chr(39)},
                {chr(39)}{values[25]}{chr(39)},
                {chr(39)}{values[26]}{chr(39)},
                {chr(39)}{values[27]}{chr(39)},
                {chr(39)}{values[28]}{chr(39)},
                {chr(39)}{values[29]}{chr(39)},
                {chr(39)}{values[30]}{chr(39)},
                {chr(39)}{values[31]}{chr(39)},
                {chr(39)}{values[32]}{chr(39)},
                cast(NEWID() as varchar(max))
            )
        """
        

    elif queryNumber == 4:
        query = """
            SELECT
                STEXT,
                BASE64FILE1,
                BASE64FILE2,
                BASE64FILE3,
                BASE64FILE4,
                BASE64FILE5,
                BASE64FILE6,
                BASE64FILE7,
                BASE64FILE8,
                BASE64FILE9,
                BASE64FILE10,
                BASE64FILE11,
                BASE64FILE12,
                BASE64FILE13,
                BASE64FILE14,
                BASE64FILE15,
                BASE64FILE16,
                BASE64FILE17,
                BASE64FILE18,
                BASE64FILE19,
                BASE64FILE20,
                BASE64FILE21,
                BASE64FILE22,
                BASE64FILE23,
                BASE64FILE24,
                BASE64FILE25,
                BASE64FILE26,
                BASE64FILE27,
                BASE64FILE28,
                BASE64FILE29,
                BASE64FILE30,
                FILENAME,
                ID,
                CREATEDBY,
                CAST(CREATEDAT AS DATE) AS CREATEDAT
            FROM
                TABLE4
            WHERE ISDELETE = 0
        """


    elif queryNumber == 5:
        query = f"""
            SELECT STEXT, FILENAME FROM TABLE4
        """


    elif queryNumber == 6:
        query = """
            WITH RankedResults AS (
                SELECT F1.DISPLAY AS NAME, 
                CASE F4.COMPANY WHEN '01' THEN 'COMPANY1' WHEN '02' THEN 'COMPANY2' WHEN '03' THEN 'COMPANY3' WHEN '04' THEN 'COMPANY4' ELSE '' END AS COMPANY, 
                CASE F4.PLANT WHEN '01' THEN 'PL1' WHEN '02' THEN 'PL2' END AS PLANT, 
                    F6.STEXT, F1.CONTACTNUM, F4.LEAVEDATE, F5.CREATEDAT, F1.EMAIL,
                    ROW_NUMBER() OVER (PARTITION BY F1.DISPLAY, F4.COMPANY, F4.PLANT, F1.CONTACTNUM ORDER BY F5.CREATEDAT DESC) AS RowNum,
                    CASE F7.BLOODTYPE WHEN 0 THEN 'BİLİNMİYOR' WHEN 1 THEN 'A rh+' WHEN 2 THEN 'A rh-' WHEN 3 THEN 'B rh+' 
                                    WHEN 4 THEN 'B rh-' WHEN 5 THEN 'AB rh+' WHEN 6 THEN 'AB rh-' WHEN 7 THEN '0 rh+' 
                                    WHEN 8 THEN '0 rh-' END AS BLOODTYPE, '' AS WIRELESSPHONE
                FROM 
                    IASADRBOOKCONTACT F1
                    INNER JOIN IASHCMPER F2 ON F2.CLIENT = F1.CLIENT AND F2.CONTACTNUM = F1.CONTACTNUM AND F2.EMPLTYPE = 0 AND F2.ISDELETED = 0
                    INNER JOIN IASHCMPER F3 ON F3.CLIENT = F2.CLIENT AND F3.CONTACTNUM = F2.CONTACTNUM
                    INNER JOIN IASADRBKCNTREC F4 ON F4.CLIENT = F3.CLIENT AND F4.CONTACTNUM = F3.CONTACTNUM AND F4.LEAVEWORKSTATUS = 0
                    INNER JOIN IASADRBKCNTWRK F5 ON F5.CLIENT = F4.CLIENT AND F5.CONTACTNUM = F4.CONTACTNUM
                    INNER JOIN IASBAS082X F6 ON F6.CLIENT = F1.CLIENT AND F6.COMPANY = F4.COMPANY AND F6.DEPARTCODE = F5.DEPARTMENT AND F6.LANGU = 'T' AND F6.PLANT = F4.PLANT
                    INNER JOIN IASADRBKCNTID F7 ON F7.CLIENT = F5.CLIENT AND F7.CONTACTNUM = F5.CONTACTNUM
                WHERE 
                    F1.CLIENT = '00'
                    AND F1.ISDELETED = 0
                    AND F1.CISCUSTORVEND = 0
            )
            SELECT DISTINCT NAME, COMPANY, PLANT, STEXT, EMAIL, BLOODTYPE, WIRELESSPHONE
            FROM RankedResults
            WHERE RowNum = 1
            ORDER BY NAME;
        """


    elif queryNumber == 7:
        query = """
        SELECT BASE64FILE1,
                BASE64FILE2,
                BASE64FILE3,
                BASE64FILE4,
                BASE64FILE5,
                BASE64FILE6,
                BASE64FILE7,
                BASE64FILE8,
                BASE64FILE9,
                BASE64FILE10,
                BASE64FILE11,
                BASE64FILE12,
                BASE64FILE13,
                BASE64FILE14,
                BASE64FILE15,
                BASE64FILE16,
                BASE64FILE17,
                BASE64FILE18,
                BASE64FILE19,
                BASE64FILE20,
                BASE64FILE21,
                BASE64FILE22,
                BASE64FILE23,
                BASE64FILE24,
                BASE64FILE25,
                BASE64FILE26,
                BASE64FILE27,
                BASE64FILE28,
                BASE64FILE29,
                BASE64FILE30
            FROM TABLE1
        """


    elif queryNumber == 8:
        query = """
        SELECT BASE64FILE1,
                BASE64FILE2,
                BASE64FILE3,
                BASE64FILE4,
                BASE64FILE5,
                BASE64FILE6,
                BASE64FILE7,
                BASE64FILE8,
                BASE64FILE9,
                BASE64FILE10,
                BASE64FILE11,
                BASE64FILE12,
                BASE64FILE13,
                BASE64FILE14,
                BASE64FILE15,
                BASE64FILE16,
                BASE64FILE17,
                BASE64FILE18,
                BASE64FILE19,
                BASE64FILE20,
                BASE64FILE21,
                BASE64FILE22,
                BASE64FILE23,
                BASE64FILE24,
                BASE64FILE25,
                BASE64FILE26,
                BASE64FILE27,
                BASE64FILE28,
                BASE64FILE29,
                BASE64FILE30
            FROM TABLE3
        """


    elif queryNumber == 9:
        query = """
        SELECT STEXT
            FROM TABLE3
        """


    elif queryNumber == 10:
        query = """
        WITH RankedResults AS (
                SELECT ISNULL(F8.USERNAME,'') AS USERNAME, F1.DISPLAY AS NAME,
                    ROW_NUMBER() OVER (PARTITION BY F1.DISPLAY, F4.COMPANY, F4.PLANT, F1.CONTACTNUM ORDER BY F5.CREATEDAT DESC) AS RowNum
                FROM 
                    IASADRBOOKCONTACT F1
                    INNER JOIN IASHCMPER F2 ON F2.CLIENT = F1.CLIENT AND F2.CONTACTNUM = F1.CONTACTNUM AND F2.EMPLTYPE = 0 AND F2.ISDELETED = 0
                    INNER JOIN IASHCMPER F3 ON F3.CLIENT = F2.CLIENT AND F3.CONTACTNUM = F2.CONTACTNUM
                    INNER JOIN IASADRBKCNTREC F4 ON F4.CLIENT = F3.CLIENT AND F4.CONTACTNUM = F3.CONTACTNUM AND F4.LEAVEWORKSTATUS = 0
                    INNER JOIN IASADRBKCNTWRK F5 ON F5.CLIENT = F4.CLIENT AND F5.CONTACTNUM = F4.CONTACTNUM
					LEFT OUTER JOIN IASUSERS F8 ON F8.CLIENT = F1.CLIENT AND F8.CONTACTNUM = F1.CONTACTNUM AND F8.ISBLOCKED = 0
                WHERE 
                    F1.CLIENT = '00'
                    AND F1.ISDELETED = 0
                    AND F1.CISCUSTORVEND = 0
            )
            SELECT DISTINCT
                CASE WHEN RIGHT((NAME + ' - ' + USERNAME), 3) = ' - ' THEN NAME ELSE (NAME + ' - ' + USERNAME) END as NAME
            FROM RankedResults
            WHERE RowNum = 1
            ORDER BY NAME;
        """


    elif queryNumber == 11:
        query = f"""
            INSERT INTO {values[0]} VALUES (
                {chr(39)}00{chr(39)},
                {chr(39)}{values[1]}{chr(39)},
                GETDATE(),
                {chr(39)}{values[1]}{chr(39)},
                GETDATE(),
                {chr(39)}{values[2]}{chr(39)},
                {chr(39)}{values[3]}{chr(39)},
                {chr(39)}{values[4]}{chr(39)},
                {chr(39)}{values[5]}{chr(39)},
                {chr(39)}{values[6]}{chr(39)},
                {chr(39)}{values[7]}{chr(39)},
                {chr(39)}{values[8]}{chr(39)},
                {chr(39)}{values[9]}{chr(39)},
                {chr(39)}{values[10]}{chr(39)},
                {chr(39)}{values[11]}{chr(39)},
                {chr(39)}{values[12]}{chr(39)},
                {chr(39)}{values[13]}{chr(39)},
                {chr(39)}{values[14]}{chr(39)},
                {chr(39)}{values[15]}{chr(39)},
                {chr(39)}{values[16]}{chr(39)},
                {chr(39)}{values[17]}{chr(39)},
                {chr(39)}{values[18]}{chr(39)},
                {chr(39)}{values[19]}{chr(39)},
                {chr(39)}{values[20]}{chr(39)},
                {chr(39)}{values[21]}{chr(39)},
                {chr(39)}{values[22]}{chr(39)},
                {chr(39)}{values[23]}{chr(39)},
                {chr(39)}{values[24]}{chr(39)},
                {chr(39)}{values[25]}{chr(39)},
                {chr(39)}{values[26]}{chr(39)},
                {chr(39)}{values[27]}{chr(39)},
                {chr(39)}{values[28]}{chr(39)},
                {chr(39)}{values[29]}{chr(39)},
                {chr(39)}{values[30]}{chr(39)},
                {chr(39)}{values[31]}{chr(39)},
                {chr(39)}{values[32]}{chr(39)}
            )
        """
    

    elif queryNumber == 12:
        query = f"DELETE FROM {values[0]}"
    

    elif queryNumber == 13:
        query = f"INSERT INTO {values[0]} VALUES ("
        query += f"{chr(39)}{str('00')}{chr(39)},"
        query += f"{chr(39)}{values[1]}{chr(39)},"
        query += "GETDATE(),"
        query += f"{chr(39)}{values[1]}{chr(39)},"
        query += "GETDATE(),"
        query += f"{chr(39)}{values[2]}{chr(39)},"
        query += f"{chr(39)}{values[3]}{chr(39)},"
        query += f"{chr(39)}{values[4]}{chr(39)},"
        query += f"{chr(39)}{values[5]}{chr(39)},"
        query += f"{chr(39)}{values[6]}{chr(39)},"
        query += f"{chr(39)}{values[7]}{chr(39)},"
        query += f"{chr(39)}{values[8]}{chr(39)},"
        query += f"{chr(39)}{values[9]}{chr(39)},"
        query += f"{chr(39)}{values[10]}{chr(39)},"
        query += f"{chr(39)}{values[11]}{chr(39)},"
        query += f"{chr(39)}{values[12]}{chr(39)},"
        query += f"{chr(39)}{values[13]}{chr(39)},"
        query += f"{chr(39)}{values[14]}{chr(39)},"
        query += f"{chr(39)}{values[15]}{chr(39)},"
        query += f"{chr(39)}{values[16]}{chr(39)},"
        query += f"{chr(39)}{values[17]}{chr(39)},"
        query += f"{chr(39)}{values[18]}{chr(39)},"
        query += f"{chr(39)}{values[19]}{chr(39)},"
        query += f"{chr(39)}{values[20]}{chr(39)},"
        query += f"{chr(39)}{values[21]}{chr(39)},"
        query += f"{chr(39)}{values[22]}{chr(39)},"
        query += f"{chr(39)}{values[23]}{chr(39)},"
        query += f"{chr(39)}{values[24]}{chr(39)},"
        query += f"{chr(39)}{values[25]}{chr(39)},"
        query += f"{chr(39)}{values[26]}{chr(39)},"
        query += f"{chr(39)}{values[27]}{chr(39)},"
        query += f"{chr(39)}{values[28]}{chr(39)},"
        query += f"{chr(39)}{values[29]}{chr(39)},"
        query += f"{chr(39)}{values[30]}{chr(39)},"
        query += f"{chr(39)}{values[31]}{chr(39)},"
        query += f"{chr(39)}{values[32]}{chr(39)},"
        query += f"{chr(39)}{values[33]}{chr(39)}"
        query += ")"


    elif queryNumber == 14:
        query = f"INSERT INTO {values[0]} VALUES ("
        query += f"{chr(39)}{str('00')}{chr(39)},"
        query += f"{chr(39)}{values[1]}{chr(39)},"
        query += "GETDATE(),"
        query += f"{chr(39)}{values[1]}{chr(39)},"
        query += "GETDATE(),"
        query += f"{chr(39)}{values[2]}{chr(39)},"
        query += f"{chr(39)}{values[3]}{chr(39)},"
        query += f"{chr(39)}{values[4]}{chr(39)},"
        query += f"{chr(39)}{values[5]}{chr(39)},"
        query += f"{chr(39)}{values[6]}{chr(39)},"
        query += f"{chr(39)}{values[7]}{chr(39)},"
        query += f"{chr(39)}{values[8]}{chr(39)},"
        query += f"{chr(39)}{values[9]}{chr(39)},"
        query += f"{chr(39)}{values[10]}{chr(39)},"
        query += f"{chr(39)}{values[11]}{chr(39)},"
        query += f"{chr(39)}{values[12]}{chr(39)},"
        query += f"{chr(39)}{values[13]}{chr(39)},"
        query += f"{chr(39)}{values[14]}{chr(39)},"
        query += f"{chr(39)}{values[15]}{chr(39)},"
        query += f"{chr(39)}{values[16]}{chr(39)},"
        query += f"{chr(39)}{values[17]}{chr(39)},"
        query += f"{chr(39)}{values[18]}{chr(39)},"
        query += f"{chr(39)}{values[19]}{chr(39)},"
        query += f"{chr(39)}{values[20]}{chr(39)},"
        query += f"{chr(39)}{values[21]}{chr(39)},"
        query += f"{chr(39)}{values[22]}{chr(39)},"
        query += f"{chr(39)}{values[23]}{chr(39)},"
        query += f"{chr(39)}{values[24]}{chr(39)},"
        query += f"{chr(39)}{values[25]}{chr(39)},"
        query += f"{chr(39)}{values[26]}{chr(39)},"
        query += f"{chr(39)}{values[27]}{chr(39)},"
        query += f"{chr(39)}{values[28]}{chr(39)},"
        query += f"{chr(39)}{values[29]}{chr(39)},"
        query += f"{chr(39)}{values[30]}{chr(39)},"
        query += f"{chr(39)}{values[31]}{chr(39)},"
        query += f"{chr(39)}{values[32]}{chr(39)},"
        query += f"{chr(39)}{values[33]}{chr(39)},"
        query += f"{chr(39)}{values[34]}{chr(39)}"
        query += ")"


    elif queryNumber == 15:
        query = f"SELECT EMPLOYEE FROM TABLE2 WHERE EMPLOYEE = {chr(39)}{values[0]}{chr(39)}"


    elif queryNumber == 16:
        query = f"UPDATE TABLE2 SET FILENAME = {chr(39)}{values[0]}{chr(39)}, BASE64FILE1 = {chr(39)}{values[1]}{chr(39)}, BASE64FILE2 = {chr(39)}{values[2]}{chr(39)}, BASE64FILE3 = {chr(39)}{values[3]}{chr(39)}, "
        query += f"BASE64FILE4 = {chr(39)}{values[4]}{chr(39)}, BASE64FILE5 = {chr(39)}{values[5]}{chr(39)}, BASE64FILE6 = {chr(39)}{values[6]}{chr(39)}, BASE64FILE7 = {chr(39)}{values[7]}{chr(39)}, "
        query += f"BASE64FILE8 = {chr(39)}{values[8]}{chr(39)}, BASE64FILE9 = {chr(39)}{values[9]}{chr(39)}, BASE64FILE10 = {chr(39)}{values[10]}{chr(39)}, BASE64FILE11 = {chr(39)}{values[11]}{chr(39)}, BASE64FILE12 = {chr(39)}{values[12]}{chr(39)}, "
        query += f"BASE64FILE13 = {chr(39)}{values[13]}{chr(39)}, BASE64FILE14 = {chr(39)}{values[14]}{chr(39)}, BASE64FILE15 = {chr(39)}{values[15]}{chr(39)}, BASE64FILE16 = {chr(39)}{values[16]}{chr(39)}, BASE64FILE17 = {chr(39)}{values[17]}{chr(39)}, BASE64FILE18 = {chr(39)}{values[18]}{chr(39)}, "
        query += f"BASE64FILE19 = {chr(39)}{values[19]}{chr(39)}, BASE64FILE20 = {chr(39)}{values[20]}{chr(39)}, BASE64FILE21 = {chr(39)}{values[21]}{chr(39)}, BASE64FILE22 = {chr(39)}{values[22]}{chr(39)}, BASE64FILE23 = {chr(39)}{values[23]}{chr(39)}, BASE64FILE24 = {chr(39)}{values[24]}{chr(39)}, "
        query += f"BASE64FILE25 = {chr(39)}{values[25]}{chr(39)}, BASE64FILE26 = {chr(39)}{values[26]}{chr(39)}, BASE64FILE27 = {chr(39)}{values[27]}{chr(39)}, BASE64FILE28 = {chr(39)}{values[28]}{chr(39)}, BASE64FILE29 = {chr(39)}{values[29]}{chr(39)}, BASE64FILE30 = {chr(39)}{values[30]}{chr(39)}, "
        query += f"CHANGEDBY = {chr(39)}{values[31]}{chr(39)}, CHANGEDAT = GETDATE() WHERE EMPLOYEE = {chr(39)}{values[32]}{chr(39)}"


    elif queryNumber == 17:
        query = f"UPDATE TABLE4 SET FILENAME = {chr(39)}{values[0]}{chr(39)}, BASE64FILE1 = {chr(39)}{values[1]}{chr(39)}, BASE64FILE2 = {chr(39)}{values[2]}{chr(39)}, BASE64FILE3 = {chr(39)}{values[3]}{chr(39)}, "
        query += f"BASE64FILE4 = {chr(39)}{values[4]}{chr(39)}, BASE64FILE5 = {chr(39)}{values[5]}{chr(39)}, BASE64FILE6 = {chr(39)}{values[6]}{chr(39)}, BASE64FILE7 = {chr(39)}{values[7]}{chr(39)}, "
        query += f"BASE64FILE8 = {chr(39)}{values[8]}{chr(39)}, BASE64FILE9 = {chr(39)}{values[9]}{chr(39)}, BASE64FILE10 = {chr(39)}{values[10]}{chr(39)}, BASE64FILE11 = {chr(39)}{values[11]}{chr(39)}, BASE64FILE12 = {chr(39)}{values[12]}{chr(39)}, "
        query += f"BASE64FILE13 = {chr(39)}{values[13]}{chr(39)}, BASE64FILE14 = {chr(39)}{values[14]}{chr(39)}, BASE64FILE15 = {chr(39)}{values[15]}{chr(39)}, BASE64FILE16 = {chr(39)}{values[16]}{chr(39)}, BASE64FILE17 = {chr(39)}{values[17]}{chr(39)}, BASE64FILE18 = {chr(39)}{values[18]}{chr(39)}, "
        query += f"BASE64FILE19 = {chr(39)}{values[19]}{chr(39)}, BASE64FILE20 = {chr(39)}{values[20]}{chr(39)}, BASE64FILE21 = {chr(39)}{values[21]}{chr(39)}, BASE64FILE22 = {chr(39)}{values[22]}{chr(39)}, BASE64FILE23 = {chr(39)}{values[23]}{chr(39)}, BASE64FILE24 = {chr(39)}{values[24]}{chr(39)}, "
        query += f"BASE64FILE25 = {chr(39)}{values[25]}{chr(39)}, BASE64FILE26 = {chr(39)}{values[26]}{chr(39)}, BASE64FILE27 = {chr(39)}{values[27]}{chr(39)}, BASE64FILE28 = {chr(39)}{values[28]}{chr(39)}, BASE64FILE29 = {chr(39)}{values[29]}{chr(39)}, BASE64FILE30 = {chr(39)}{values[30]}{chr(39)}, "
        query += f"CHANGEDBY = {chr(39)}{values[31]}{chr(39)}, CHANGEDAT = GETDATE() WHERE CAST(ID AS VARCHAR(MAX)) = {chr(39)}{values[32]}{chr(39)}"


    elif queryNumber == 18:
        query = f"UPDATE TABLE4 SET STEXT = {chr(39)}{values[0]}{chr(39)},  "
        query += f"CHANGEDBY = {chr(39)}{values[1]}{chr(39)}, CHANGEDAT = GETDATE() WHERE CAST(ID AS VARCHAR(MAX)) = {chr(39)}{values[2]}{chr(39)}"


    elif queryNumber == 19:
        query = f"UPDATE TABLE4 SET ISDELETE = 1 WHERE CAST(ID AS VARCHAR(MAX)) = {chr(39)}{values[0]}{chr(39)}; DELETE FROM TABLE5 WHERE CAST(ID AS VARCHAR(MAX)) = {chr(39)}{values[0]}{chr(39)}"


    elif queryNumber == 20:
        query = "SELECT * FROM TABLE4 WHERE ISDELETE = 0 AND "
        query += f"FILENAME = {chr(39)}{values[0]}{chr(39)} AND CAST(BASE64FILE1 AS VARCHAR(MAX)) = {chr(39)}{values[1]}{chr(39)} AND CAST(BASE64FILE2 AS VARCHAR(MAX)) = {chr(39)}{values[2]}{chr(39)} AND CAST(BASE64FILE3 AS VARCHAR(MAX)) = {chr(39)}{values[3]}{chr(39)} AND "
        query += f"CAST(BASE64FILE4 AS VARCHAR(MAX)) = {chr(39)}{values[4]}{chr(39)} AND CAST(BASE64FILE5 AS VARCHAR(MAX)) = {chr(39)}{values[5]}{chr(39)} AND CAST(BASE64FILE6 AS VARCHAR(MAX)) = {chr(39)}{values[6]}{chr(39)} AND CAST(BASE64FILE7 AS VARCHAR(MAX)) = {chr(39)}{values[7]}{chr(39)} AND "
        query += f"CAST(BASE64FILE8 AS VARCHAR(MAX)) = {chr(39)}{values[8]}{chr(39)} AND CAST(BASE64FILE9 AS VARCHAR(MAX)) = {chr(39)}{values[9]}{chr(39)} AND CAST(BASE64FILE10 AS VARCHAR(MAX)) = {chr(39)}{values[10]}{chr(39)} AND CAST(BASE64FILE11 AS VARCHAR(MAX)) = {chr(39)}{values[11]}{chr(39)} AND CAST(BASE64FILE12 AS VARCHAR(MAX)) = {chr(39)}{values[12]}{chr(39)} AND "
        query += f"CAST(BASE64FILE13 AS VARCHAR(MAX)) = {chr(39)}{values[13]}{chr(39)} AND CAST(BASE64FILE14 AS VARCHAR(MAX)) = {chr(39)}{values[14]}{chr(39)} AND CAST(BASE64FILE15 AS VARCHAR(MAX)) = {chr(39)}{values[15]}{chr(39)} AND CAST(BASE64FILE16 AS VARCHAR(MAX)) = {chr(39)}{values[16]}{chr(39)} AND CAST(BASE64FILE17 AS VARCHAR(MAX)) = {chr(39)}{values[17]}{chr(39)} AND CAST(BASE64FILE18 AS VARCHAR(MAX)) = {chr(39)}{values[18]}{chr(39)} AND "
        query += f"CAST(BASE64FILE19 AS VARCHAR(MAX)) = {chr(39)}{values[19]}{chr(39)} AND CAST(BASE64FILE20 AS VARCHAR(MAX)) = {chr(39)}{values[20]}{chr(39)} AND CAST(BASE64FILE21 AS VARCHAR(MAX)) = {chr(39)}{values[21]}{chr(39)} AND CAST(BASE64FILE22 AS VARCHAR(MAX)) = {chr(39)}{values[22]}{chr(39)} AND CAST(BASE64FILE23 AS VARCHAR(MAX)) = {chr(39)}{values[23]}{chr(39)} AND CAST(BASE64FILE24 AS VARCHAR(MAX)) = {chr(39)}{values[24]}{chr(39)} AND "
        query += f"CAST(BASE64FILE25 AS VARCHAR(MAX)) = {chr(39)}{values[25]}{chr(39)} AND CAST(BASE64FILE26 AS VARCHAR(MAX)) = {chr(39)}{values[26]}{chr(39)} AND CAST(BASE64FILE27 AS VARCHAR(MAX)) = {chr(39)}{values[27]}{chr(39)} AND CAST(BASE64FILE28 AS VARCHAR(MAX)) = {chr(39)}{values[28]}{chr(39)} AND CAST(BASE64FILE29 AS VARCHAR(MAX)) = {chr(39)}{values[29]}{chr(39)} AND CAST(BASE64FILE30 AS VARCHAR(MAX)) = {chr(39)}{values[30]}{chr(39)} AND "
        query += f"STEXT = {chr(39)}{values[31]}{chr(39)}"


    elif queryNumber == 21:
        query = f"INSERT INTO TABLE5 VALUES ("
        query += f"{chr(39)}{values[0]}{chr(39)},"
        query += f"{chr(39)}{str('00')}{chr(39)},"
        query += f"{chr(39)}{values[1]}{chr(39)}, 0,"
        query += f"{chr(39)}{values[2]}{chr(39)},"
        query += "GETDATE(),"
        query += f"{chr(39)}{values[2]}{chr(39)},"
        query += "GETDATE(),"
        query += f"{chr(39)}{values[3]}{chr(39)},"

        i = 1
        while i <= 29:
            query += f"{chr(39)}{values[i + 3]}{chr(39)},"
            i += 1
            
        query += f"{chr(39)}{values[33]}{chr(39)}"
        query += ")"

    elif queryNumber == 22:
        query = f"""SELECT ID FROM TABLE5 WHERE ISDELETE = 0 
                        AND CAST(ID AS VARCHAR(MAX)) = {chr(39)}{values[0]}{chr(39)}"""
        
    elif queryNumber == 23:
        query = f"UPDATE TABLE5 SET FILENAME = "
        query += f"{chr(39)}{values[0]}{chr(39)}, STEXT = "
        query += f"{chr(39)}{values[1]}{chr(39)}, "

        i = 1
        while i <= 30:
            query += f"BASE64FILE" + str(i)
            query += f" = CAST({chr(39)}{values[i+1]}{chr(39)}AS VARCHAR(MAX)), "
            i += 1
        
        query += f"CHANGEDBY = {chr(39)}{values[32]}{chr(39)}, "
        query += f"CHANGEDAT = GETDATE() "
        query += f"WHERE CAST(ID AS VARCHAR(MAX)) = {chr(39)}{values[33]}{chr(39)}"

    elif queryNumber == 24:
        query = f"""SELECT ID,CLIENT,STEXT,ISDELETE,CREATEDBY,CREATEDAT,CHANGEDBY,CHANGEDAT,
                        FILENAME,BASE64FILE1,BASE64FILE2,BASE64FILE3,BASE64FILE4,BASE64FILE5,
                        BASE64FILE6,BASE64FILE7,BASE64FILE8,BASE64FILE9,BASE64FILE10,
                        BASE64FILE11,BASE64FILE12,BASE64FILE13,BASE64FILE14,BASE64FILE15,
                        BASE64FILE16,BASE64FILE17,BASE64FILE18,BASE64FILE19,BASE64FILE20,
                        BASE64FILE21,BASE64FILE22,BASE64FILE23,BASE64FILE24,BASE64FILE25,
                        BASE64FILE26,BASE64FILE27,BASE64FILE28,BASE64FILE29,BASE64FILE30 
                        FROM TABLE5 WHERE ISDELETE = 0 
                        AND CAST(ID AS VARCHAR(MAX)) = {chr(39)}{values[0]}{chr(39)}"""
        
    elif queryNumber == 25:
        query = f"""SELECT ID,CLIENT,STEXT,ISDELETE,CREATEDBY,CREATEDAT,CHANGEDBY,CHANGEDAT,
                        FILENAME,BASE64FILE1,BASE64FILE2,BASE64FILE3,BASE64FILE4,BASE64FILE5,
                        BASE64FILE6,BASE64FILE7,BASE64FILE8,BASE64FILE9,BASE64FILE10,
                        BASE64FILE11,BASE64FILE12,BASE64FILE13,BASE64FILE14,BASE64FILE15,
                        BASE64FILE16,BASE64FILE17,BASE64FILE18,BASE64FILE19,BASE64FILE20,
                        BASE64FILE21,BASE64FILE22,BASE64FILE23,BASE64FILE24,BASE64FILE25,
                        BASE64FILE26,BASE64FILE27,BASE64FILE28,BASE64FILE29,BASE64FILE30 
                        FROM TABLE4 WHERE ISDELETE = 0 
                        AND CAST(ID AS VARCHAR(MAX)) = {chr(39)}{values[0]}{chr(39)}"""
        
    elif queryNumber == 26:
        query = f"""
            DECLARE @SAY AS INT

            SELECT @SAY = COUNT(*)
                FROM TABLE4
                WHERE ISDELETE = 0
                AND CAST(ID AS VARCHAR(MAX)) <> {chr(39)}{values[0]}{chr(39)}

            IF @SAY > 2
            BEGIN
                SELECT TOP 2 ID, STEXT, BASE64FILE1,BASE64FILE2,BASE64FILE3,BASE64FILE4,BASE64FILE5,
                                    BASE64FILE6,BASE64FILE7,BASE64FILE8,BASE64FILE9,BASE64FILE10,
                                    BASE64FILE11,BASE64FILE12,BASE64FILE13,BASE64FILE14,BASE64FILE15,
                                    BASE64FILE16,BASE64FILE17,BASE64FILE18,BASE64FILE19,BASE64FILE20,
                                    BASE64FILE21,BASE64FILE22,BASE64FILE23,BASE64FILE24,BASE64FILE25,
                                    BASE64FILE26,BASE64FILE27,BASE64FILE28,BASE64FILE29,BASE64FILE30
                    FROM TABLE4 
                    WHERE ISDELETE = 0 
                    AND CAST(ID AS VARCHAR(MAX)) <> {chr(39)}{values[0]}{chr(39)}
                    ORDER BY CREATEDAT DESC
            END

            ELSE IF @SAY = 2
            BEGIN
                SELECT TOP 2 ID, STEXT, BASE64FILE1,BASE64FILE2,BASE64FILE3,BASE64FILE4,BASE64FILE5,
                                    BASE64FILE6,BASE64FILE7,BASE64FILE8,BASE64FILE9,BASE64FILE10,
                                    BASE64FILE11,BASE64FILE12,BASE64FILE13,BASE64FILE14,BASE64FILE15,
                                    BASE64FILE16,BASE64FILE17,BASE64FILE18,BASE64FILE19,BASE64FILE20,
                                    BASE64FILE21,BASE64FILE22,BASE64FILE23,BASE64FILE24,BASE64FILE25,
                                    BASE64FILE26,BASE64FILE27,BASE64FILE28,BASE64FILE29,BASE64FILE30 
                    FROM TABLE4 
                    WHERE ISDELETE = 0 
                    ORDER BY CREATEDAT DESC
            END

            ELSE
            BEGIN
                SELECT ID, STEXT, BASE64FILE1,BASE64FILE2,BASE64FILE3,BASE64FILE4,BASE64FILE5,
                                    BASE64FILE6,BASE64FILE7,BASE64FILE8,BASE64FILE9,BASE64FILE10,
                                    BASE64FILE11,BASE64FILE12,BASE64FILE13,BASE64FILE14,BASE64FILE15,
                                    BASE64FILE16,BASE64FILE17,BASE64FILE18,BASE64FILE19,BASE64FILE20,
                                    BASE64FILE21,BASE64FILE22,BASE64FILE23,BASE64FILE24,BASE64FILE25,
                                    BASE64FILE26,BASE64FILE27,BASE64FILE28,BASE64FILE29,BASE64FILE30 
                    FROM TABLE4 
                    WHERE ISDELETE = 0
                UNION ALL
                SELECT ID, STEXT, BASE64FILE1,BASE64FILE2,BASE64FILE3,BASE64FILE4,BASE64FILE5,
                                    BASE64FILE6,BASE64FILE7,BASE64FILE8,BASE64FILE9,BASE64FILE10,
                                    BASE64FILE11,BASE64FILE12,BASE64FILE13,BASE64FILE14,BASE64FILE15,
                                    BASE64FILE16,BASE64FILE17,BASE64FILE18,BASE64FILE19,BASE64FILE20,
                                    BASE64FILE21,BASE64FILE22,BASE64FILE23,BASE64FILE24,BASE64FILE25,
                                    BASE64FILE26,BASE64FILE27,BASE64FILE28,BASE64FILE29,BASE64FILE30
                    FROM TABLE4 
                    WHERE ISDELETE = 0
            END
        """
        
    return query