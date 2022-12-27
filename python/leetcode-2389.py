# 2389. Longest Subsequence With Limited Sum
# test case

nums = [4,5,2,1]
queries = [3,10,21]
# Output: [2,3,4]

nums = [469781,45635,628818,324948,343772,713803,452081]
queries = [816646,929491]
# Output : [3,3]


nums = [892599,557543,351931,28539,914656,226726,255449,750741,807018,754851,461978,503963,670830,543588,783085,902220,892934,783097,777077,297312,881986,939694,230760,58103,93541,436890,651916,511113,425460,579016,934683,373773,366190,16028,560664,325276,663537,838668,236788,464923,92876,318889,492084,207073,761207,217917,701331,654295,851964,838377,786795,981896,558708,717973,65230,670142,984233,92776,372940,248992,60888,926786,621678,849972,141580,4284,511055,657900,169605,411442,375293,487428,246453,303333]
queries = [960435,469562,405444,741272,29763,923470,616544,809077,525521,829276,834301,954592,927708,432064,450407,715286,726201,831853,143722,501222,886968,655046,131292,678097,84782,168884,437696,539466,477830,588513,640937,514810,932188,397158,425992,841880,577217,457738,27436,952706,469180,124308,638834,118943,451584,829357,586928,392838,528190,118124,572503,796518,58713,73756,563199,731385,250039,971896,282224,406121,651859,490091,929474,283927,548880,72607,359619,613327,261651,325524,672437,138659,380023,528060,335010,339589,184688,642091,159211,680411,564531,868161,730660,631338,682033,559082,384605,646474,812902,633297,883040,621673,228385]

# Output : [11,8,7,10,2,11,9,10,9,11,11,11,11,8,8,10,10,11,4,8,11,10,4,10,3,5,8,9,8,9,9,9,11,7,8,11,9,8,2,11,8,4,9,4,8,11,9,7,9,4,9,10,3,3,9,10,6,11,6,7,9,8,11,6,9,3,7,9,6,6,10,4,7,9,7,7,5,9,4,10,9,11,10,9,10,9,7,9,10,9,11,9,5]


nums = [172856,227236,799457,705733,827346,653202,848115,537748,172204,179967,777377,748333,167067,23722,571684,922222,396885,988560,65430,179347,324983,608554,525306,958647,701263,987627,759714,732175,13989,385714,670907,774770,461177,821793,571813,345156,518151,217602,105254,244500,625881,206040,504870,473789,559400,873658,556452,562568,69212,44443,610461,282689,23686,865042,171169,181213,818148,39261,580383,607765,492235,374565,85530,655494,740058,492397,910514,964731,256691,306011,46669,598361,217127,645942,512688,641603,702091,350805,247321,433954,594213,188796,852789,249034,111652,839101,111164,634969,324719,337856,390011,838718,307383,136923,767021,57807,317322,36435,902658,996089,790624,800554,689577,307211,312028,722612,880729,332080,111250,853411,781243,914990,922948,176469,724991,495522,964136,77907,928204,181776,361700,641529,640299,89172,698053,379067,225991,962341,30003,362802,309955,446572,838501,340380,903774,366174,253932,687850,999128,739038,886721,956044,541571,185388,527539,429405,944971,266629,479353,22359,142149,151561,64419,437975,850656,262600,188340,79060,160029,634186,655092,903538,364841,607664,991227,101922,698727,540924,456891,234753,346399,372745,664534,296147,441475,690560,705014,880141,240386,472390,668207,56836,456121,254553,531892,840189,295401,724985,884100,215706,933525,12503,978120,65025,693032,952698,462463,108764,789189,982911,518133,884471,680285,631401,103394,362117,791578,439004,707101,670496,865808,682110,618393,733461,115318,46686,209579,905386,86002,718187,836836,697522,859500,845047,887165,698064,245421,252431,217234,315375,697817,318458,831181,489669,545238,349592,495562,161157,542091,809190,154637,398376,687095,612680,488819,325703,386575,129897,985310,603749,225337,29792,909364,588979,790331,67645,628404,328960,436438,157019,611804,200522,12482,266765,423857,936505,161944,100392,65825,156970,616724,873702,567943,265254,510365,621520,557647,74086,739865,627521,214325,138934,437757,737860,352702,481273,588245,742747,992214,745441,275154,287696,591795,75711,698557,755112,683494,495069,220542,109414,891818,389739,780756,699094,354233,260606,252211,877487,283742,52191,184936,88937,324276,362120,735258,71855,261175,66924,948914,213481,321132,14090,466718,521105,121830,538882,480049,89912,855746,932357,467273,470944,807267,647406,179246,433060,339302,971017,534316,17821,144937,883913,484948,494363,588995,794705,128317,884029,630756,102148,928804,92176,344256,193495,889005,926173,97266,209853,774765,382066,623027,759624,522186,471729,690336,954924,782281,305414,419749,205914,660719,395625,626504,975687,841047,106188,846017,693710,234710,100840,760148,209393,929345,497377,167770,439594,5064,626836,337422,31631,141590,776976,992793,784512,170680,105646,164785,162912,57581,451858,37227,31587,574547,590775,873902,828350,180873,378707,987716,791124,129529,709371,617813,39078,286015,750832,520865,433810,231058,751965,248573,396200,919849,926241,600922,448129,304907,257732,968847,64973,489620,899164,423951,411958,567796,914671,959583,274864,332027,368394,988569,96230,353592,99974,350129,961585,222876,923401,592977,194706,508945,573803,467311,560582,318907,20019,861342,436013,155516,773017,616528,832938,87356,559402,977400,521735,976507,771074,9395,982086,741930,480628,971274,942762,472976,344691,786159,732389,463898,786805,775462,55282,458576,563770,25890,405671,569807,97789,115236,70510,48722,422958,270407,34969,626715,379757,879695,40856,587599,468416,531840,881639,400424,769350,932520,733233,874062,387662,941781,260756,818695,525013,951128,511600,738040,133687,548596,423156,196597,950221,927511,91571,279146,87043,673458,541916,376350,644483,204613,96974,158506,933929,195173,491228,930745,484011,322751,166794,218102,256443,663769,949128,326433,762725,468327,937760,687765,379364,957348,664751,165929,584977,499918,970330,922215,302345,516488,48863,351581,887573,381748,125365,991048,905735,525889,92437,846345,48309,351643,755472,153705,521450,281084,242505,922674,171950,525924,297604,1208,145686,329443,330040,605510,724290,660396,623037,158775,304160,793798,616215,115058,777200,22772,976089,667199,258704,186339,590085,683244,909656,185311]
queries = [637059,4960,978244,984113,817852,947262,329145,307559,527429,891447,815676,784713,811123,287558,322118,908317,364579,596830,123539,155752,612804,929366,799279,577233,661943,898762,533922,181971,67632,204576,980237,243384,551598,319405,451844,2461,528617,800001,427104,544787,691927,116682,630550,774090,422313,601977,685474,59740,451260,812019,98511,542039,789216,478830,319855,865559,46644,59765,25878,486869,495755,837310,84896,368266,653942,277990,211229,968905,760753,123190,444826,729526,871437,714071,223806,179551,887424,818519,700026,710084,524563,873786,410455,982455,446778,999305,400516,493160,644830,885484,230291,796235,970033,494036,615262,1219,664473,910615,407963,64156,323530,228562,244507,395119,968782,799250,186625,878931,995665,692327,966889,662902,94614,341060,246072,924747,635816,66067,104649,181103,434606,83106,150332,314118,862543,955810,243628,18845,563074,554305,70168,35547,843654,651537,366902,573425,798994,549688,823807,337935,518129,239179,880311,96547,31240,815429,13532,348364,269745,200145,456058,531138,568194,56517,436944,430161,535819,502355,8766,430860,836079,293063,28859,443603,233245,533416,742999,222579,501029,63897,786381,194976,769348,968112,765717,653405,793685,473285,662318,847863,478430,738603,912576,5715,478214,282478,408209,647511,616786,514382,302549,324939,916776,139623,742855,298907,825632,121689,848936,529916,307219,707869,436376,280503,224325,966557,736256,661014,451368,875613,869991,440639,478343,940158,284118,492838,621068,997527,278952,773708,169177,976075,971097,866760,781855,269606,637122,504685,434311,405315,772198,994625,249320,755688,136331,639763,4735,55674,815331,48768,527270,411605,49968,602668,671874,508153,848996,491711,926284,830772,437163,124614,552444,317188,570436,711655,580635,298812,484040,366098,254252,8204,610555,700394,273721,698449,732273,287133,709554,262017,361803,488655,839106,774572,415799,918605,492069,763685,556683,840516,872170,227827,715326,203579,14631,639347,999969,426561,324503,489840,6503,665993,829504,26764,624468,177654,564481,17152,670913,707925,386806,432095,683576,195828,353118,753433,747759,807425,718806,538951,539410,691390,402699,804620,803102,481509,734936,534555,385722,727521,141014,178808,571169,892760,726320,764642,652142,558086,929137,888423,660036,834581,715966,529743,935463,232564,943871,624310,249994,459481,720371,645171,353129,252381,152811,487359,705257,230042,115706,786826,188386,230678,667168,786864,172869,950041,92182,625157,293653,228301,71337,819592,725843,754098,114976,360016,100024,734720,696309,73410,412811,756041,839818,864523,52703,877814,12907,5971,337554,329456,594628,298752,701854,701845,885814,482280,881485,614452,291753,391658,550062,424315,174093,229982,301487,355312,568833,742128,238358,661357,818193,105912,754842,882632,509492,212891,99242,533442,231942,413433,425584,252492,965156,663691,234444,24204,65445,537197,367264,845576,724269,643234,401187,789576,160976,369696,257476,966688,39343,108795,194743,294872,519566,538907,309618,792349,767058,849790,391839,496329,519772,780904,277061,171205,719291,755785,295549,118013,874245,507895,161074,980040,908540,47070,115203,125785,157843,403433,102854,978042,836487,402587,787300,701658,880343,131257,154363,397142,400816,184004,121209,738646,507414,740370,545879,476363,69236,539245,997662,786877,984295,120867,193597,814365,196188,448360,590124,896140,443364,544443,749849,16415,769431,126935,461524,270790,595050,393798,342876,753070,137495,539234,268360,284450,755435,941381,777969,595859,317549,837582,238960,824511,512247,878334,754204,609930,469813,631010,907140,119250,171202,351795,585001,835077,361102,813042,970944,864060,238338,487778,396213,968765,115722,563090,354984,241843,178698,380842,131236,172736,788103,610682,238579,601207,500319,388257,607503,788714,964936,625189,445792,387790,877900,168417,288820,369279,181168,200443,536975,977679,461583,681481,643231,256605,25199,699632,731352,661752,245596,502989,844141,562955,621154,740506,846642,546707,570986,321955,159614,482195,175619,765581,984623,784877,903838,499139,271160,465476,682096,770137,39114,393859,648770,609587,264406,771125,733986,419858,123152,467169,601979,510127,368694,788684,798925,753957,258030,112823,667555,313623,359818,756798,485508,6158,317740,208062,821324,240009,114034,610920,435019,892059,365609,154068,46749,429253,663112,301745,433003,24464,893968,850758,271802,991725,972569,619033,702851,288664,178196,469972,344987,158614,373009,607332,343135,406044,411475,782817,281259,505250,360512,941888,967667,247269,989044,588911,806810,96651,86721,437242,652044,968810,805176,304032,541955,783566,347784,894593,520784,462019,350668,120267,385452,691253,559997,846154,481792,582775,961783,60863,207552,240046,284144,542922,119136,154014,398850,729453,401152,526806,663119,53928,239524,234234,214327,531116,373552,987144,94992,923402,586591,837999,708345,268227,248705,586070,995822,293562,172306,601103,626130,68921,546797,188654,384660,451148,302487,332,326058,774584,294521,848283,289243,608882,997986,995135,266956,720868,717818,224425,843579,490829,969166,817872,151098,579825,676751,389651,537206,546313,948645,655090,170992,155417,654475,640264,540251,511731,9920,732113,241877,802298,940080,739519,322785,645107,890269,503895,939247,520684,285134,713149,619302,410574,819237,199608,715349,683774,801214,572753,373211,27094,253709,601899,621223,76746,847829,719296,684690,75118,25875,278246,904817,991773,917297,255933,947496,680773,504311,769078,774223,117264,701910,430582,786361,790896,940748,894645,202539,845958,905066,477621,296564,895514,506635,495246,76836,885102,212488,485770,791126,5606,892323,194041,303808,578084,193316,318844,796888,604167,931342,612536,834621,210667,127795,410013,938017,166565,356570,144948,230337,558064,718822,707756,517124,803707,607882,467428,180952,835511,155118,42896,661827,968756,227395,256733,160704,55795,150316,47767,197209,625345,911871,273297,894056,248935,259887,271828,755195,955808,661113,114519,496350,611845,85533,134921,363542,61426,238434,607557,898965,547162,520444,503723,564932,142744,50526,896951,244868,570897,931511,189413,220388,251143,126436,661005,22950,861766,714127,781651,908827,933913,624979,440345,509644,410232,127346,576827,636306,857160,889323,704941,634456,680253,513871,273316,312622,359568,697366,765244,281240,57193,340047,296239,484085,231075,445835,929075,234501,115778,89651,793968,598269,143642,224531,637994,67309,486388,306186,140013,743501,200770,547866,672157,559203,933862,511298,548057,522996,360768,322454,159614,44729]

# [25,1,32,32,29,31,17,16,22,30,29,28,29,16,17,30,18,24,9,11,24,31,28,24,25,30,22,12,6,13,32,14,23,17,20,1,22,28,20,23,26,9,25,28,20,24,26,6,20,29,8,23,28,21,17,30,5,6,3,21,22,29,7,18,25,15,13,32,27,9,20,27,30,27,13,12,30,29,26,26,22,30,19,32,20,32,19,21,25,30,14,28,32,21,24,1,25,30,19,6,17,14,14,19,32,28,12,30,32,26,31,25,8,17,14,31,25,6,8,12,20,7,10,16,30,31,14,3,23,23,7,4,29,25,18,23,28,23,29,17,22,14,30,8,4,29,2,18,15,13,20,22,23,6,20,20,23,22,2,20,29,16,4,20,14,22,27,13,22,6,28,12,28,32,28,25,28,21,25,29,21,27,31,1,21,15,19,25,24,22,16,17,31,10,27,16,29,9,29,22,16,26,20,15,13,31,27,25,20,30,30,20,21,31,15,21,25,32,15,28,11,32,32,30,28,15,25,22,20,19,28,32,14,27,10,25,1,6,29,5,22,19,5,24,26,22,29,21,31,29,20,9,23,17,23,26,24,16,21,18,14,2,24,26,15,26,27,16,26,15,18,21,29,28,19,31,21,28,23,29,30,14,27,13,2,25,32,20,17,21,2,25,29,3,25,12,23,3,26,26,19,20,26,12,18,27,27,28,27,23,23,26,19,28,28,21,27,22,19,27,10,12,23,30,27,28,25,23,31,30,25,29,27,22,31,14,31,25,14,21,27,25,18,14,11,21,26,14,9,28,12,14,26,28,11,31,8,25,16,14,7,29,27,27,9,18,8,27,26,7,19,27,29,30,5,30,2,1,17,17,24,16,26,26,30,21,30,24,16,19,23,20,11,14,16,18,23,27,14,25,29,8,27,30,22,13,8,22,14,19,20,14,31,25,14,3,6,23,18,29,27,25,19,28,11,18,15,31,4,9,12,16,22,23,16,28,28,29,19,22,22,28,15,11,27,27,16,9,30,22,11,32,30,5,9,9,11,19,8,32,29,19,28,26,30,10,11,19,19,12,9,27,22,27,23,21,7,23,32,28,32,9,12,29,12,20,24,30,20,23,27,3,28,9,21,15,24,19,17,27,10,23,15,15,27,31,28,24,17,29,14,29,22,30,27,24,21,25,30,9,11,18,24,29,18,29,32,30,14,21,19,32,9,23,18,14,12,18,10,11,28,24,14,24,22,19,24,28,31,25,20,19,30,11,16,18,12,13,23,32,21,26,25,15,3,26,27,25,14,22,29,23,25,27,29,23,23,17,15,21,12,28,32,28,30,22,15,21,26,28,4,19,25,24,15,28,27,20,9,21,24,22,18,28,28,27,15,9,26,16,18,27,21,1,17,13,29,14,9,24,20,30,18,11,5,20,25,16,20,3,30,29,15,32,32,24,26,16,12,21,17,11,18,24,17,19,19,28,15,22,18,31,32,14,32,24,28,8,8,20,25,32,28,16,23,28,17,30,22,21,18,9,19,26,23,29,21,24,31,6,13,14,15,23,9,11,19,27,19,22,25,5,14,14,13,22,18,32,8,31,24,29,26,15,14,24,32,16,11,24,25,7,23,12,19,20,16,0,17,28,16,29,16,24,32,32,15,27,27,13,29,21,32,29,10,24,26,19,23,23,31,25,11,11,25,25,23,22,2,27,14,28,31,27,17,25,30,22,31,22,16,26,24,19,29,13,27,26,28,23,18,3,14,24,25,7,29,27,26,7,3,15,30,32,31,15,31,26,22,28,28,9,26,20,28,28,31,30,13,29,30,21,16,30,22,21,7,30,13,21,28,1,30,12,16,24,12,17,28,24,31,24,29,13,9,19,31,11,18,10,14,23,27,26,22,28,24,21,12,29,11,5,25,32,14,15,11,6,10,5,12,25,31,15,30,14,15,15,27,31,25,9,22,24,7,10,18,6,14,24,30,23,22,22,23,10,5,30,14,23,31,12,13,14,9,25,3,30,27,28,30,31,25,20,22,19,9,24,25,29,30,26,25,26,22,15,16,18,26,28,15,6,17,16,21,14,20,31,14,9,8,28,24,10,13,25,6,21,16,10,27,13,23,26,23,31,22,23,22,18,17,5]
# [25,1,32,32,29,31,17,16,22,30,29,28,29,16,17,30,18,24,9,11,24,31,28,24,25,30,22,12,6,13,32,14,23,17,20,1,22,28,20,23,26,9,25,28,20,24,26,6,20,29,8,23,28,21,17,30,5,6,3,21,22,29,7,18,25,15,13,32,27,9,20,27,30,27,13,12,30,29,26,26,22,30,19,32,20,32,19,21,25,30,14,28,32,21,24,1,25,30,19,6,17,14,14,19,32,28,12,30,32,26,31,25,8,17,14,31,25,6,8,12,20,7,10,16,30,31,14,3,23,23,7,4,29,25,18,23,28,23,29,17,22,14,30,8,4,29,2,18,15,13,20,22,23,6,20,20,23,22,2,20,29,16,4,20,14,22,27,13,22,6,28,12,28,32,28,25,28,21,25,29,21,27,31,1,21,15,19,25,24,22,16,17,31,10,27,16,29,9,29,22,16,26,20,15,13,31,27,25,20,30,30,20,21,31,15,21,25,32,15,28,11,32,32,30,28,15,25,22,20,19,28,32,14,27,10,25,1,6,29,5,22,19,5,24,26,22,29,21,31,29,20,9,23,17,23,26,24,16,21,18,14,2,24,26,15,26,27,16,26,15,18,21,29,28,19,31,21,28,23,29,30,14,27,13,2,25,32,20,17,21,2,25,29,3,25,12,23,3,26,26,19,20,26,12,18,27,27,28,27,23,23,26,19,28,28,21,27,22,19,27,10,12,23,30,27,28,25,23,31,30,25,29,27,22,31,14,31,25,14,21,27,25,18,14,11,21,26,14,9,28,12,14,26,28,11,31,8,25,16,14,7,29,27,27,9,18,8,27,26,7,19,27,29,30,5,30,2,1,17,17,24,16,26,26,30,21,30,24,16,19,23,20,11,14,16,18,23,27,14,25,29,8,27,30,22,13,8,22,14,19,20,14,31,25,14,3,6,23,18,29,27,25,19,28,11,18,15,31,4,9,12,16,22,23,16,28,28,29,19,22,22,28,15,11,27,27,16,9,30,22,11,32,30,5,9,9,11,19,8,32,29,19,28,26,30,10,11,19,19,12,9,27,22,27,23,21,7,23,32,28,32,9,12,29,12,20,24,30,20,23,27,3,28,9,21,15,24,19,17,27,10,23,15,15,27,31,28,24,17,29,14,29,22,30,27,24,21,25,30,9,11,18,24,29,18,29,32,30,14,21,19,32,9,23,18,14,12,18,10,11,28,24,14,24,22,19,24,28,31,25,20,19,30,11,16,18,12,13,23,32,21,26,25,15,3,26,27,25,14,22,29,23,25,27,29,23,23,17,11,21,12,28,32,28,30,22,15,21,26,28,4,19,25,24,15,28,27,20,9,21,24,22,18,28,28,27,15,9,26,16,18,27,21,1,17,13,29,14,9,24,20,30,18,11,5,20,25,16,20,3,30,29,15,32,32,24,26,16,12,21,17,11,18,24,17,19,19,28,15,22,18,31,32,14,32,24,28,8,8,20,25,32,28,16,23,28,17,30,22,21,18,9,19,26,23,29,21,24,31,6,13,14,15,23,9,11,19,27,19,22,25,5,14,14,13,22,18,32,8,31,24,29,26,15,14,24,32,16,11,24,25,7,23,12,19,20,16,0,17,28,16,29,16,24,32,32,15,27,27,13,29,21,32,29,10,24,26,19,23,23,31,25,11,11,25,25,23,22,2,27,14,28,31,27,17,25,30,22,31,22,16,26,24,19,29,13,27,26,28,23,18,3,14,24,25,7,29,27,26,7,3,15,30,32,31,15,31,26,22,28,28,9,26,20,28,28,31,30,13,29,30,21,16,30,22,21,7,30,13,21,28,1,30,12,16,24,12,17,28,24,31,24,29,13,9,19,31,11,18,10,14,23,27,26,22,28,24,21,12,29,11,5,25,32,14,15,11,6,10,5,12,25,31,15,30,14,15,15,27,31,25,9,22,24,7,10,18,6,14,24,30,23,22,22,23,10,5,30,14,23,31,12,13,14,9,25,3,30,27,28,30,31,25,20,22,19,9,24,25,29,30,26,25,26,22,15,16,18,26,28,15,6,17,16,21,14,20,31,14,9,8,28,24,10,13,25,6,21,16,10,27,13,23,26,23,31,22,23,22,18,17,11,5]

class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        
        # sorted_queries :list[int] = sorted(queries)
        sorted_nums :list[int] = sorted(nums, reverse=True)
        max_subseq :dict[int, list[int]] = dict()
        answer :list[int] = list()
        
        
        for limit in queries:
            
            max_subseq[limit] = []
                    
                
        for num in sorted_nums:
            
            for limit in max_subseq:
                
                if sum(max_subseq[limit]) + num > limit:
                    if (sum(max_subseq[limit][1:]) + num) <= limit and max_subseq[limit][0] >= num:
                        max_subseq[limit] = max_subseq[limit][1:] + [num]
                    
                else:
                    max_subseq[limit].append(num)
                    
        
        
        return [len(max_subseq[x]) for x in queries]
        

# main 
if __name__ == "__main__":
    
    a = Solution()
    
    # insert method here
    print(a.answerQueries(nums=nums, queries=queries))