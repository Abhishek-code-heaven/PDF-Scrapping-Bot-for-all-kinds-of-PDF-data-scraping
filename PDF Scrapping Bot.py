#from tabula import read_pdf
import PyPDF2
def PDFScrappingBot(x):


    pdfFileObj = open(x, 'rb')
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # printing number of pages in pdf file
    pages = pdfReader.numPages
    # creating a page object
    pdfdata = []
    for y in range(pages):
        pageObj = pdfReader.getPage(y)
        # extracting text from page
        ss = pageObj.extractText()
        pdfdata.append(ss)
        # closing the pdf file object
    pdfFileObj.close()
    pdfdata = ' '.join(pdfdata)

    try:
        acknowledgementnumberoriginalreturn = pdfdata.split("Acknowledgement Number :")[1].split("\n")[0].strip()
    except:
        acknowledgementnumberoriginalreturn = None
        pass
    try:
        firstname = pdfdata.split("First Name\n")[1].split("\n")[0]

    except:
        pass
    try:
        middlename = pdfdata.split("Middle Name\n")[1].split("\n")[0]

    except:
        pass
    try:
        lastname = pdfdata.split("Last Name\n")[1].split("\n")[0]

    except:
        pass
    try:
        name = firstname + " " + middlename + " " + lastname

    except:
        pass
    try:
        dateofbirth = pdfdata.split("Date of Birth / Formation (DD/MM/YYYY)\n")[1].split("\n")[0]

    except:
        pass
    try:
        status = pdfdata.split("Status\n")[1].split("\n")[0]

    except:
        pass
    try:
        fathername = pdfdata.split("son/ daughter of \n")[1].split("\n")[0]

    except:
        pass
    try:
        aadharcardnumber = pdfdata.split("Filing portal. Applicable to Individual only.)\n")[1].split("\n")[0]

    except:
        aadharcardnumber = None
        pass
    try:
        aadharenrollmentnumber = pdfdata.split("and time of enrolment to be entered\ncontinuously)")[1].split("\n")[0]

    except:
        aadharenrollmentnumber = None
        pass
    try:
        pan = pdfdata.split("PAN\n")[1].split("\nD")[0]

    except:
        pass
    try:
        residencename = pdfdata.split("Name of Premises / Building / Village\n")[1].split("\n")[0]

    except:
        pass
    try:
        roadorstreet = pdfdata.split("Road / Street / Post Office\n")[1].split("\n")[0]

    except:
        pass
    try:
        localityorarea = pdfdata.split("Area / Locality\n")[1].split("\n")[0]

    except:
        pass
    try:
        cityortownordistrict = pdfdata.split("Town / City / District\n")[1].split("\n")[0]

    except:
        pass
    try:
        statecode = pdfdata.split("State\n")[1].split("\n")[0]

    except:
        pass
    try:
        country = pdfdata.split("Country\n")[1].split("\n")[0]

    except:
        pass
    try:
        pincode = pdfdata.split("Pin code\n")[1].split("\n")[0]

    except:
        pass
    try:
        emailaddress = pdfdata.split("Email Address - 1(Self)\n")[1].split("\n")[0]

    except:
        pass
    try:
        mobilenumber = pdfdata.split("Mobile no.1\n")[1].split("\n")[0].strip()

    except:
        pass
    try:
        residentialstatus = pdfdata.split("Residential Status\n")[1].split("\n")[0]

    except:
        pass
    try:
        originalreturnfilingdate = None

    except:
        pass
    try:
        revisedreturnfilingdate = None

    except:
        pass
    try:
        bankaccountnumber = pdfdata.split("\nprefer to get\nyour refund\ncredited\n1\n")[1].split("\nb)")[0].split("\n")[-1]

    except:
        pass
    try:
        bankname = pdfdata.split("\nprefer to get\nyour refund\ncredited\n1\n")[1].split("\nb)")[0].split("\n")[-2]

    except:
        pass
    try:
        ifscode = pdfdata.split("\nprefer to get\nyour refund\ncredited\n1\n")[1].split("\nb)")[0].split("\n")[0]

    except:
        pass
    try:
        din = pdfdata.split("Number (DIN)\n1\n")[1].split("\nW")[0].split("\n")[-1]

    except:
        din = None
        pass
    try:
        nameofcompany = pdfdata.split("Number (DIN)\n1\n")[1].split("\n")[0]

    except:
        nameofcompany = None
        pass
    try:
        typeofcompany = pdfdata.split("Number (DIN)\n1\n")[1].split("\n")[1]



    except:
        typeofcompany = None
        pass
    try:
        panofcompany = pdfdata.split("Number (DIN)\n1\n")[1].split("\nW")[0].split("\n")[-3]
    except:
        panofcompany = None
        pass
    try:
        sharestype = None

    except:
        pass
    try:
        grosssalary = pdfdata.split("Total gross salary from all employers (1)\n")[1].split("\n3")[0]

    except:
        grosssalary = None
        pass
    try:
        netsalaryt = pdfdata.split("Net Salary (2 Œ 3)\n")[1].split("\n5")[0]
        if len(netsalaryt) < 3 or len(netsalaryt) > 10:
            netsalaryt = None
        else:
            netsalary = netsalaryt


    except:
        pass
    try:
        totaldeductions = pdfdata.split("Deduction u/s 16 (5a + 5b + 5c)\n")[1].split("\n5")[0]

    except:
        totaldeductions = None
        pass
    try:
        taxableincomefromsalaryt = pdfdata.split("Income chargeable under the Head ‚Salaries™ (4-5)\n")[1].split("\n")[0]

    except:


        pass
    try:
        if len(taxableincomefromsalaryt) < 3 or len(taxableincomefromsalaryt) > 10:
            taxableincomefromsalaryt = None
        else:
            taxableincomefromsalary = taxableincomefromsalaryt

    except:
        pass
    try:
        passthroughincome = '0'

    except:
        pass
    try:
        arrearsorunrealizedrentreceived = None
        rentarrear = None
        shorttermgainonimmovableproperty = None

    except:
        pass
    try:
        stcgonequityshareforother = pdfdata.split("paid) (2c +2d)\nA2e\n")[1].split("\n")[0]

    except:
        stcgonequityshareforother = None
        pass
    try:
        stcgonequityshareforforeigninvestors = stcgonequityshareforother

    except:
        stcgonequityshareforforeigninvestors = None
        pass
    try:
        nritaxsecuritiestransactiontaxpaid = pdfdata.split("transaction tax (STT) is paid\nA3a\n")[1].split("\n3")[0]

    except:
        pass
    try:
        nritaxsecuritiestransactiontaxnotpaid = pdfdata.split("transaction tax (STT) is not paid\nA3b\n")[1].split("\n")[0]

    except:
        pass
    try:
        shorttermgainonsaleofsecurities = pdfdata.split("(other than those at A2) (4c +4d)\nA4e\n")[1].split("\n")[0]

    except:
        pass
    try:
        shorttermgainonotherassets = pdfdata.split("A1 or A2 or A3 or A4 above (5c + 5d)\nA5e\n")[1].split("\n")[0]

    except:
        pass
    try:
        longtermgainonimmovableproperty = None
        longtermgainonbondordebenture = pdfdata.split("LTCG on bonds or debenture (2c Œ 2d)\nB2e\n")[1].split("\n3")[0]

    except:
        pass
    try:
        longtermgainonsaleoflistedsecurities = pdfdata.split("Long-term Capital Gains on assets at B3 above (3c Œ 3d)\nB3e\n")[1].split("\n4")[0]

    except:
        longtermgainonsaleoflistedsecurities = None
        pass
    try:
        longtermgainonequityshares = pdfdata.split("Long-term Capital Gains on sale of capital assets at B4 above (4c Œ 4e)\n4f\n")[1].split("\n")[0]

    except:
        longtermgainonequityshares = None
        pass
    try:
        longtermgainonsaleofsharesordebentures = pdfdata.split("LTCG on share or debenture (5a Œ 5b)\n")[1].split("B5c\n")[1].split("\n")[0]

    except:
        pass
    try:
        ltcgonsaleofspecifiedassets = pdfdata.split("Balance LTCG on sale of specified asset (6a Œ 6b)\nB8c\n")[1].split("\n")[0]

    except:
        pass
    try:
        ltcgonsaleofotherthanspecifiedassets = pdfdata.split("Balance LTCG on sale of specified asset (6a Œ 6b)\nB8c\n")[1].split("\nd")[0]

    except:
        pass
    try:
        longtermgainonotherassets = pdfdata.split("Balance LTCG on sale of asset, other than specified asset (8d Œ 8e)\nB8f\n")[1].split("\n")[0]

    except:
        pass
    try:
        incomefromdividends = '0'
        incomefrominterest = '0'

    except:
        pass

    try:
        rentfrommachineryplantandbuilding = pdfdata.split("Rental income from machinery, plants, buildings, etc.,\nGross\n1c\n")[1].split("\n")[0]

    except:
        pass
    try:
        incomefromimmovableproperty = pdfdata.split("(di + dii + diii + div + dv)\n1d\n")[1].split("\nd")[0]

    except:
        pass
    try:
        anyotherincome = None
        anyotherincomegross = None

    except:
        pass
    try:
        incomechargeableatspecialrates = pdfdata.split("Income chargeable at special rates (2a + 2b + 2c + 2d + 2e + 2f elements related to Sl. No. 1)\n2\n")[1].split("\na")[0]

    except:
        pass
    try:
        incomefromowningandmaintainingracehorses = pdfdata.split("(if negative take the figure to 6xi of Schedule CFL)\ne\n")[1].split("\n9")[0]

    except:
        pass
    try:
        incomefromwinninglotteries = None
        dividendincomefromdomesticcompany = None
        deemedincomechareabletotax = None
        incomefrompatentchargeable = None
        otherincomechargeableatspecifiedrate = None

    except:
        pass
    try:
        deductionundersectionfiftyseven = pdfdata.split(" only)\naii\n0\nb\nDepreciation\nb\n0\nc\nTotal\nc\n")[1].split("\n4")[0]

    except:
        pass
    try:
        amountnotdeductibleundersectionfiftyeight = pdfdata.split("Amounts not deductible u/s 58\n4\n")[1].split("\n5")[0]

    except:
        pass
    try:
        profitcharegabletotaxundersectionfiftynine = pdfdata.split("Profits chargeable to tax u/s 59\n5\n")[1].split("\nP")[0]

    except:
        pass
    try:
        incomechargeableatnormalrates = pdfdata.split("(If negative take the figure to 3xi of schedule CYLA)\n6\n")[1].split("\n7")[0]

    except:
        pass
    try:
        incomefromsalary = pdfdata.split("Salaries (6 of Schedule S)\n1\n")[1].split("\n")[0]

    except:
        pass
    try:
        incomefromhouseproperty = pdfdata.split("Income from house property (4 of Schedule-HP) (Enter nil if loss)\n2\n")[1].split("\n")[0]

    except:
        pass
    try:


        gainsfrombusinessandprofession = None

    except:

        pass
    try:
        shorttermcapitalgain = pdfdata.split("Total Short term (ai+aii+aiii+aiv)\n3av\n")[1].split("\nb")[0]

    except:
        shorttermcapitalgain = None
        pass
    try:
        longtermcapitalgain = pdfdata.split("Total Long-term (bi + bii+biii) (enter nil if loss)\n3biv\n")[1].split("\n")[0]

    except:
        pass
    try:
        incomefromothersources = pdfdata.split("Total (4a + 4b + 4c) \n (enter nil if loss)\n4d\n")[1].split("\n5")[0]

    except:
        incomefromothersources = None
        pass
    try:
        totalofheadwiseincome = pdfdata.split("Total of head wise income (1+2+3c+4d)\n5\n")[1].split("\n6")[0]

    except:
        pass
    try:
        lossesofcurrentyear = pdfdata.split("(2xiii and 3xiii) of Schedule CYLA)\n6\n")[1].split("\n7")[0]

    except:
        pass
    try:
        broughtforwardlosses = pdfdata.split("Brought forward losses set off against 7(2xii of Schedule BFLA)\n8\n")[1].split("\n9")[0]

    except:
        pass
    try:
        grosstotalincome = pdfdata.split("(3xiii of Schedule BFLA + 2 of Schedule OS)\n9\n")[1].split("\n10")[0]

    except:
        pass
    try:
        totalchapterviadeductions = pdfdata.split("Deductions under Chapter VI-A [u of Schedule VIA and limited to(9-10)]\n11\n")[1].split("\n12")[0]

    except:
        pass
    try:
        incomechargeabletotaxatspecialrate = pdfdata.split("tax at special rates (total of column (i) of schedule SI)\n13\n")[1].split("\n14")[0]

    except:
        pass
    try:
        netagriculturalincome = pdfdata.split("any other income for rate purpose (3 of Schedule EI)\n14\n")[1].split("\n15")[0]

    except:
        pass
    try:

        deemedincomeundersectiononehundredfifteen = pdfdata.split("Deemed income under section 115JC (3 of schedule AMT)\n17\n")[1].split("\nP")[0]
    except:
        deemedincomeundersectiononehundredfifteen = None
    totaltaxpayable = pdfdata.split("Tax payable on deemed total income under section 115JC (4 of Schedule AMT)\n1a\n")[1].split("\n1b")[0]
    rebateundereightysevena = pdfdata.split("Rebate under section 87A\n3\n")[1].split("\n4")[0]
    taxpayableonrebate = pdfdata.split("Tax payable after rebate (2d - 3)\n4\n")[1].split("\n5\n")[0]
    totalsurcharge = pdfdata.split("Total i + ii\n4iii\n")[1].split("\n")[0]
    healthandeducationcess = pdfdata.split("Health and Education cess @4% on (4 + 5(iii) )\n6\n")[1].split("\n7")[0]
    grosstaxliability = pdfdata.split("Gross tax liability (4 + 5(iii) + 6)\n7\n")[1].split("\n8")[0]
    try:
        grosstaxpayable = pdfdata.split("Gross tax payable (higher of 1d and 7)\n8\n")[1].split("\n9")[0]
    except:
        grosstaxpayable = None
    try:
        creditundersectiononeonefivejdorjaa = pdfdata.split("(applicable if 7 is more than 1d)(5 of Schedule\nAMTC)\n9\n")[1].split("\n10")[0]
    except:
        creditundersectiononeonefivejdorjaa = None

    totaltaxrelief = pdfdata.split("Total (11a + 11b + 11c)\n11d\n")[1].split('\nNe')[0]
    try:
        nettaxliability = pdfdata.split("(10 Œ 11d) (enter zero if negative)\n12\n")[1].split("\n13")[0]
    except:
        nettaxliability = None
    totaltaxinterestandfeepayable = pdfdata.split("Total Interest and Fee Payable (13a+13b+13c+13d)\n13e\n")[1].split("\n14")[0]
    aggregateliability = pdfdata.split("Aggregate liability (12 + 13e)\n14\n")[1].split("\n15")[0]
    totaltds = pdfdata.split("TDS (total of column 5 of 22B and column 9 of 22C)\n")[1].split("\nc")[0]
    balancetaxpayable = pdfdata.split("(Enter if 14 is greater than 15e, else enter 0)\n")[1].split("\n17")[0]
    refunddue = pdfdata.split("into the bank account) .\n")[1].split("\nB")[0]
    tanofemployer = pdfdata.split("\nTotal Tax Deducted\n1\n")[1].split("\n")[0]
    nameofdeductor = None
    panofotherpersonotherthansalary = None
    tdsonincomeotherthansalary = None
    nameoftenantorbuyer = None
    tdsfromimmovableproperty = None
    nameofcollector = pdfdata.split("\nxyz\nxyz\nVERIFICATION\nxyz\nI, \n")[1].split("\n")[0]
    tcs = None

    dic = {}
    dic["formname"] = formname
    returntype = None
    dic["returntype"] = returntype
    #acknowledgementnumberoriginalreturn = None
    dic["acknowledgementnumberoriginalreturn"] = acknowledgementnumberoriginalreturn
    dic["name"] = name
    dic["firstname"] = firstname
    dic["middlename"] = middlename
    dic["lastname"] = lastname
    dic["dateofbirth"] = dateofbirth
    dic["fathername"] = fathername
    employercategory = None
    dic["employercategory"] = employercategory
    #aadharcardnumber = None
    dic["aadharcardnumber"] = aadharcardnumber
    #aadharenrollmentnumber = None
    dic["aadharenrollmentnumber"] = aadharenrollmentnumber

    dic["pan"] = pan
    residencenumber = None
    dic["residencenumber"] = residencenumber

    dic["residencename"] = residencename
    dic["roadorstreet"] = roadorstreet
    # localityorarea = None
    dic["localityorarea"] = localityorarea

    dic["cityortownordistrict"] = cityortownordistrict
    dic["statecode"] = statecode
    dic["country"] = country
    dic["pincode"] = pincode
    address =   residencename + roadorstreet + localityorarea + cityortownordistrict + statecode + country + pincode
    dic["address"] = address
    dic["emailaddress"] = emailaddress
    countrycodemobile = None
    dic["mobilenumber"] = mobilenumber
    dic["formname"] = formname
    dic["residentialstatus"] = residentialstatus
    countryofresidence = None
    taxpayeridentificationnumber = None
    dic["taxpayeridentificationnumber"] = taxpayeridentificationnumber

    dic["originalreturnfilingdate"] = originalreturnfilingdate
    dic["revisedreturnfilingdate"] = revisedreturnfilingdate
    dic["status"] = status

    dic["bankaccountnumber"] = bankaccountnumber
    bankaccountnumber1 = None
    dic["bankaccountnumber"] = bankaccountnumber1
    dic["bankname"] = bankname
    bankname1 = None
    dic["bankname"] = bankname1
    dic["ifscode"] = ifscode
    ifscode1 = None
    dic["ifscode"] = ifscode1
    #din = None
    dic["din"] = din
    #nameofcompany = None
    dic["nameofcompany"] = nameofcompany
    #typeofcompany = None
    dic["typeofcompany"] = typeofcompany
    #panofcompany = None
    dic["panofcompany"] = panofcompany
    sharestype = None
    dic["sharestype"] = sharestype
    employername = None
    # dic["employername"] = employername

    # dic["name"] = name
    addressdetail = None
    # dic["addressdetail"] = addressdetail

    # dic["cityortownordistrict"] = cityortownordistrict
    employerstatecode = None
    # dic["employerstatecode"] = employerstatecode
    employerpincode = None
    # dic["employerpincode"] = employerpincode
    employerstan = None
    # dic["employerstan"] = employerstan
    panofemployer = None
    #grosssalary = None
    dic[" grosssalary "] = grosssalary
    allowancesnotexempt = None
    dic[" allowancesnotexempt "] = allowancesnotexempt
    perquisitesvalue = None
    dic["perquisitesvalue"] = perquisitesvalue
    profitsinsalary = None
    dic["profitsinsalary"] = profitsinsalary
    #netsalary = None
    dic[" netsalary "] = netsalary
    #totaldeductions = None
    dic["totaldeductions"] = totaldeductions
    #taxableincomefromsalary = None
    dic["taxableincomefromsalary"] = taxableincomefromsalary
    #passthroughincome = None
    dic["passthroughincome"] = passthroughincome
    # arrearsorunrealizedrentreceived = None
    dic["arrearsorunrealizedrentreceived"] = arrearsorunrealizedrentreceived
    rentarrear = None
    dic["rentarrear"] = rentarrear
    dic["shorttermgainonimmovableproperty"] = shorttermgainonimmovableproperty
    #stcgonequityshareforother = None
    dic["stcgonequityshareforother"] = stcgonequityshareforother
    #stcgonequityshareforforeigninvestors = None
    dic["stcgonequityshareforforeigninvestors"] = stcgonequityshareforforeigninvestors
    dic["nritaxsecuritiestransactiontaxpaid"] = nritaxsecuritiestransactiontaxpaid
    nritaxsecuritiestransactiontaxpaid1 = None
    dic["nritaxsecuritiestransactiontaxpaid"] = nritaxsecuritiestransactiontaxpaid1
    dic["shorttermgainonsaleofsecurities"] = shorttermgainonsaleofsecurities
    dic["shorttermgainonotherassets"] = shorttermgainonotherassets
    dic["longtermgainonimmovableproperty"] = longtermgainonimmovableproperty

    dic["longtermgainonbondordebenture"] = longtermgainonbondordebenture
    #longtermgainonsaleoflistedsecurities = None
    dic["longtermgainonsaleoflistedsecurities"] = longtermgainonsaleoflistedsecurities
    #longtermgainonequityshares = None
    dic["longtermgainonsaleofsharesordebentures"] = longtermgainonsaleofsharesordebentures

    dic["ltcgonsaleofspecifiedassets"] = ltcgonsaleofspecifiedassets

    dic["longtermgainonotherassets"] = longtermgainonotherassets

    dic["incomefromdividends"] = incomefromdividends

    dic["incomefrominterest"] = incomefrominterest

    dic["rentfrommachineryplantandbuilding"] = rentfrommachineryplantandbuilding
    # incomefromimmovableproperty = None
    dic["incomefromimmovableproperty"] = incomefromimmovableproperty
    anyotherincome = None
    dic["anyotherincome"] = anyotherincome

    dic["anyotherincomegross"] = anyotherincomegross

    dic["incomechargeableatspecialrates"] = incomechargeableatspecialrates

    dic["incomefromowningandmaintainingracehorses"] = incomefromowningandmaintainingracehorses
    incomefromwinninglotteries = None
    dic["incomefromwinninglotteries"] = incomefromwinninglotteries
    dividendincomefromdomesticcompany = None
    dic["dividendincomefromdomesticcompany"] = dividendincomefromdomesticcompany
    deemedincomechareabletotax = None
    dic["deemedincomechareabletotax"] = deemedincomechareabletotax
    incomefrompatentchargeable = None
    dic["incomefrompatentchargeable"] = incomefrompatentchargeable
    otherincomechargeableatspecifiedrate = None
    dic["otherincomechargeableatspecifiedrate"] = otherincomechargeableatspecifiedrate

    dic["deductionundersectionfiftyseven"] = deductionundersectionfiftyseven
    # amountnotdeductibleundersectionfiftyeight = None
    dic["amountnotdeductibleundersectionfiftyeight"] = amountnotdeductibleundersectionfiftyeight
    # profitcharegabletotaxundersectionfiftynine = None
    dic["profitcharegabletotaxundersectionfiftynine"] = profitcharegabletotaxundersectionfiftynine

    dic["incomechargeableatnormalrates"] = incomechargeableatnormalrates

    dic["incomefromsalary"] = incomefromsalary

    dic["incomefromhouseproperty"] = incomefromhouseproperty
    #gainsfrombusinessandprofession = None
    dic["gainsfrombusinessandprofession"] = gainsfrombusinessandprofession
    #shorttermcapitalgain = None
    dic["shorttermcapitalgain"] = shorttermcapitalgain

    dic["longtermcapitalgain"] = longtermcapitalgain
    #incomefromothersources = None
    dic["incomefromothersources"] = incomefromothersources

    dic["totalofheadwiseincome"] = totalofheadwiseincome
    # lossesofcurrentyear = None
    dic["lossesofcurrentyear"] = lossesofcurrentyear

    dic["broughtforwardlosses"] = broughtforwardlosses

    dic["grosstotalincome"] = grosstotalincome
    # totalchapterviadeductions = None

    dic["totalchapterviadeductions"] = totalchapterviadeductions
    totaltaxableincome = None
    dic["totaltaxableincome"] = totaltaxableincome

    dic["incomechargeabletotaxatspecialrate"] = incomechargeabletotaxatspecialrate

    dic["netagriculturalincome"] = netagriculturalincome
    aggregateincome  = None
    dic["aggregateincome"] = aggregateincome
    #deemedincomeundersectiononehundredfifteen = None
    dic["deemedincomeundersectiononehundredfifteen"] = deemedincomeundersectiononehundredfifteen
    # totaltaxpayable = None
    dic["totaltaxpayable"] = totaltaxpayable
    dic["rebateundereightysevena"] = rebateundereightysevena

    dic["taxpayableonrebate"] = taxpayableonrebate

    dic["totalsurcharge"] = totalsurcharge

    dic["healthandeducationcess"] = healthandeducationcess

    dic["grosstaxliability"] = grosstaxliability
    #grosstaxpayable = None
    dic["grosstaxpayable"] = grosstaxpayable
    #creditundersectiononeonefivejdorjaa = None
    dic["creditundersectiononeonefivejdorjaa"] = creditundersectiononeonefivejdorjaa
    taxpayableaftercreditundersectionhundredfifteenjdorjaa = None
    dic[
        "taxpayableaftercreditundersectionhundredfifteenjdorjaa"] = taxpayableaftercreditundersectionhundredfifteenjdorjaa

    dic["totaltaxrelief"] = totaltaxrelief
    #nettaxliability = None
    dic["nettaxliability"] = nettaxliability

    dic["totaltaxinterestandfeepayable"] = totaltaxinterestandfeepayable
    dic["aggregateliability"] = aggregateliability
    dic["totaltds"] = totaltds
    advancetax = None
    dic["advancetax"] = advancetax
    selfassessmenttax  = None
    dic["selfassessmenttax"] = selfassessmenttax

    dic["totaltcs"] = totaltds
    totaltaxespaid = None
    dic["totaltaxespaid"] = totaltaxespaid

    dic["balancetaxpayable"] = balancetaxpayable

    dic["refunddue"] = refunddue

    dic["tanofemployer"] = tanofemployer
    nameofemployer = None
    dic["nameofemployer"] = nameofemployer
    tdsfromsalary = None
    dic["tdsfromsalary"] = tdsfromsalary
    tanofdeductor = None
    dic["tanofdeductor"] = tanofdeductor

    dic["nameofdeductor"] = nameofdeductor
    panofotherpersonotherthansalary = None
    dic["panofotherpersonotherthansalary"] = panofotherpersonotherthansalary

    dic["tdsonincomeotherthansalary"] = tdsonincomeotherthansalary
    panoftenantorbuyer = None
    dic["panoftenantorbuyer"] = panoftenantorbuyer
    panofotherperson = None
    dic["panofotherperson"] = panofotherperson

    dic["nameoftenantorbuyer"] = nameoftenantorbuyer

    dic["tdsfromimmovableproperty"] = tdsfromimmovableproperty
    taxcollectionaccountnumber = None
    dic["taxcollectionaccountnumber"] = taxcollectionaccountnumber

    dic["nameofcollector"] = nameofcollector

    dic["tcs"] = tcs
    return dic
