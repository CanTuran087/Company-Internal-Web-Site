from flask import Flask, jsonify
import query

def ifMethod(methodNumber, *values):
    startIndex = 0
    endIndex = 65535
    substrings = []

    if methodNumber == 1:
        for say in range(0, 30):
            substring = values[0][startIndex:endIndex]
            substrings.append(substring)
            startIndex = endIndex
            endIndex += 65535

        try:
            conn = values[2]
            cursor = conn.cursor()
            cursor.execute(query.sqlQuery(12, "TABLE1") + "; " + query.sqlQuery(11, "TABLE1", values[3], values[4], substrings[0], substrings[1], substrings[
                        2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11]
                        , substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                        , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                        , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]))
            conn.commit()
            return jsonify({"success": True})

        except Exception as e:
            print("Hata: ", str(e))
            conn.rollback()
            return jsonify({"success": False, "message": "Veri eklenirken hata oluştu."})

        finally:
            conn.close()

    if methodNumber == 2:
        startIndex = 0
        endIndex = 65535
        substrings = []

        for say in range(0, 30):
            substring = values[0][startIndex:endIndex]
            substrings.append(substring)
            startIndex = endIndex
            endIndex += 65535

        try:
            conn = values[1]
            cursor = conn.cursor()

            cursor.execute(query.sqlQuery(15, values[3]))
            employeeControl = cursor.fetchall()

            if employeeControl != []:
                cursor.execute(query.sqlQuery(16, values[5], substrings[0], substrings[1], substrings[
                        2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11], 
                        substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                        , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                        , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]
                        , values[2], values[3]))
            else:
                cursor.execute(query.sqlQuery(14, "TABLE2", values[2], values[3], values[4], values[5], substrings[0], substrings[1], substrings[
                        2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11]
                        , substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                        , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                        , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]))

            conn.commit()
            return jsonify({"success": True})

        except Exception as e:
            print("Hata: ", str(e))
            conn.rollback()
            return jsonify({"success": False, "message": "Veri eklenirken hata oluştu."})

        finally:
            conn.close()

    if methodNumber == 3:
        conn = values[1]
        cursor = conn.cursor()
        startIndex = 0
        endIndex = 65535
        substrings = []

        for say in range(0, 30):
            substring = values[0][startIndex:endIndex]
            substrings.append(substring)
            startIndex = endIndex
            endIndex += 65535

        try:
            conn = values[1]
            cursor = conn.cursor()
            cursor.execute(query.sqlQuery(12, "TABLE3") + "; " + query.sqlQuery(13, "TABLE3", values[2], values[3], values[4], substrings[0], substrings[1], substrings[
                        2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11]
                        , substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                        , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                        , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]))
            conn.commit()
            return jsonify({"success": True})

        except Exception as e:
            print("Hata: ", str(e))
            conn.rollback()
            return jsonify({"success": False, "message": "Veri eklenirken hata oluştu."})

        finally:
            conn.close()

    if methodNumber == 4:
        conn = values[1]
        cursor = conn.cursor()
        startIndex = 0
        endIndex = 65535
        substrings = []

        for say in range(0, 30):
            substring = values[0][startIndex:endIndex]
            substrings.append(substring)
            startIndex = endIndex
            endIndex += 65535

        try:
            conn = values[1]
            cursor = conn.cursor()

            print(query.sqlQuery(20, values[4], '', '', '', 
                        '', '', '', '', '', '', '', '', '', 
                        '', '', '', '', '', ''
                        , '', '', '', '', '', ''
                        , '', '', '', '', '', ''
                        , values[2]))
            
            cursor.execute(query.sqlQuery(20, values[4], substrings[0], substrings[1], substrings[
                        2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11], 
                        substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                        , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                        , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]
                        , values[2]))
            announcementControl = cursor.fetchall()

            if announcementControl == []:
                cursor.execute(query.sqlQuery(3, values[2], values[3], values[4]
                            , substrings[0], substrings[1], substrings[2], substrings[3], substrings[4], substrings[5]
                            , substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11]
                            , substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                            , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                            , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]))
            conn.commit()
            return jsonify({"success": True})

        except Exception as e:
            print("Hata: ", str(e))
            conn.rollback()
            return jsonify({"success": False, "message": "Veri eklenirken hata oluştu."})

        finally:
            conn.close()

    if methodNumber == 5:
        conn = values[1]
        cursor = conn.cursor()
        startIndex = 0
        endIndex = 65535
        substrings = []

        for say in range(0, 30):
            substring = values[0][startIndex:endIndex]
            substrings.append(substring)
            startIndex = endIndex
            endIndex += 65535

        try:
            conn = values[1]
            cursor = conn.cursor()

            if values[5] != '' and values[0] != '':
                cursor.execute(query.sqlQuery(17, values[4], substrings[0], substrings[1], substrings[
                            2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11]
                            , substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                            , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                            , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]
                            , values[3], values[5]))
                
            if values[5] != '' and values[2] != '' and values[2] != '<br>':
                cursor.execute(query.sqlQuery(18, values[2], values[3], values[5]))

            conn.commit()
            return jsonify({"success": True})

        except Exception as e:
            print("Hata: ", str(e))
            conn.rollback()
            return jsonify({"success": False, "message": "Veri eklenirken hata oluştu."})

        finally:
            conn.close()

    if methodNumber == 6:
        conn = values[0]
        cursor = conn.cursor()
        print(query.sqlQuery(19, values[1]))

        try:
            conn = values[0]
            cursor = conn.cursor()
            
            cursor.execute(query.sqlQuery(19, values[1]))

            conn.commit()
            return jsonify({"success": True})

        except Exception as e:
            print("Hata: ", str(e))
            conn.rollback()
            return jsonify({"success": False, "message": "Veri eklenirken hata oluştu."})

        finally:
            conn.close()

    if methodNumber == 7:
        conn = values[0]
        cursor = conn.cursor()
        substrings = []
        announcementControl = []
        print("Method Number: 7")
        
        print(query.sqlQuery(21, '', values[3], values[7], values[2], '', '', '', 
                        '', '', '', '', '', '', '', '', '', 
                        '', '', '', '', '', ''
                        , '', '', '', '', '', ''
                        , '', '', '', '', '', ''))

        try:
            conn = values[0]
            cursor = conn.cursor()
            startIndex = 0
            endIndex = 65535

            for say in range(0, 30):
                substring = values[4][startIndex:endIndex]
                substrings.append(substring)
                startIndex = endIndex
                endIndex += 65535

            print("adım 1")
            
            cursor.execute(query.sqlQuery(20, values[6], substrings[0], substrings[1], substrings[
                        2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11], 
                        substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                        , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                        , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]
                        , values[5]))
            
            announcementControl = cursor.fetchone()

            if announcementControl:
                announcementID = announcementControl[38]
                print("announcementID : " + announcementID)

                substrings = []
                startIndex = 0
                endIndex = 65535
                
                for say in range(0, 30):
                    substring = values[1][startIndex:endIndex]
                    substrings.append(substring)
                    startIndex = endIndex
                    endIndex += 65535

                print("adım 2")

                cursor.execute(query.sqlQuery(22, announcementID))
                announcementDetailControl = cursor.fetchone()
                announcementDetailID = announcementDetailControl[0]

                if str(announcementDetailID) == "":
                    print("GELMEDİ" + announcementDetailID)
                    
                    cursor.execute(query.sqlQuery(21, announcementID, values[3], values[7], values[2], substrings[0], substrings[1], substrings[
                            2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11], 
                            substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                            , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                            , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]))
                else:
                    print("GELDİ announcementDetailID = " + announcementDetailID 
                          + " \n announcementID =" + announcementID)
                    
                    print(query.sqlQuery(23, values[2], values[3], '', '', '', 
                        '', '', '', '', '', '', '', '', '', 
                        '', '', '', '', '', ''
                        , '', '', '', '', '', ''
                        , '', '', '', '', '', ''
                        , values[7], announcementID))
                    
                    cursor.execute(query.sqlQuery(23, values[2], values[3], substrings[0], substrings[1], substrings[
                            2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11], 
                            substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                            , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                            , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]
                            , values[7], announcementID))

            else:

                substrings = []
                startIndex = 0
                endIndex = 65535

                for say in range(0, 30):
                    substring = values[4][startIndex:endIndex]
                    substrings.append(substring)
                    startIndex = endIndex
                    endIndex += 65535

                print("adım 3 \n values4 = "+'values[4]'+" \n values5 = "+values[5]+" \n values6 = "+values[6]+" \n values7 = "+values[7])

                cursor.execute(query.sqlQuery(3, values[5], values[7], values[6]
                            , substrings[0], substrings[1], substrings[2], substrings[3], substrings[4], substrings[5]
                            , substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11]
                            , substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                            , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                            , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]))
                
                print("adım 4")

                cursor.execute(query.sqlQuery(20, values[6], substrings[0], substrings[1], substrings[
                        2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11], 
                        substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                        , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                        , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]
                        , values[5]))
            
                announcementControl = cursor.fetchone()
                announcementID = announcementControl[38]

                substrings = []
                startIndex = 0
                endIndex = 65535

                for say in range(0, 30):
                    substring = values[1][startIndex:endIndex]
                    substrings.append(substring)
                    startIndex = endIndex
                    endIndex += 65535

                print("adım 5")

                cursor.execute(query.sqlQuery(21, announcementID, values[3], values[7], values[2], substrings[0], substrings[1], substrings[
                        2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11], 
                        substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                        , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                        , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]))

            conn.commit()
            return jsonify({"success": True})

        except Exception as e:
            print("Hata: ", str(e))
            conn.rollback()
            return jsonify({"success": False, "message": "Veri eklenirken hata oluştu."})

        finally:
            conn.close()

    if methodNumber == 8:
        
        for say in range(0, 30):
            substring = values[1][startIndex:endIndex]
            substrings.append(substring)
            startIndex = endIndex
            endIndex += 65535

        try:
            conn = values[0]
            cursor = conn.cursor()

            if values[1] != '' and values[2] != '' and values[3] != '' and values[3] != '<br>':
                cursor.execute(query.sqlQuery(23, values[2], values[3], substrings[0], substrings[1], substrings[
                                                2], substrings[3], substrings[4], substrings[5], substrings[6], substrings[7], substrings[8], substrings[9], substrings[10], substrings[11], 
                                                substrings[12], substrings[13], substrings[14], substrings[15], substrings[16], substrings[17]
                                                , substrings[18], substrings[19], substrings[20], substrings[21], substrings[22], substrings[23]
                                                , substrings[24], substrings[25], substrings[26], substrings[27], substrings[28], substrings[29]
                                                , values[8], values[6]))
            else:
                print("Boş Alanları Doldurunuz !")

            conn.commit()
            return jsonify({"success": True})

        except Exception as e:
            print("Hata: ", str(e))
            conn.rollback()
            return jsonify({"success": False, "message": "Veri eklenirken hata oluştu."})

        finally:
            conn.close()