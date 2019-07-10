# constants for OLD simulation # IGNORE THIS

KEYSIZE = 512
TRANSACTIONS = {
    "ingress": 0,
    "miner": 1,
    "request_expulsion": 2,
    "expulsion": 3,
}
BLOOM_MAX_ELEMENTS = 5  #number of elements that the filter holds (deve ser testado)
MINER_SLEEP_SIGNATURE_RANGE = 1

number_of_nodes = 100
miners_rate = 10

############################################################## OLD Simulation
#######
#####
###
##
#


################### Gabriel Simulator PARAMS ###################

initial_nodes = 6006
simulation_steps = 3600000


block_generated_flow =  [5000, 13000, 19000, 25000, 32000, 39000, 44000, 51000, 58000, 64000, 70000, 77000, 84000, 89000, 96000, 103000, 112000, 119000, 124000, 129000, 137000, 139000, 147000, 152000, 155000, 159000, 164000, 167000, 175000, 182000, 187000, 195000, 200000, 206000, 212000, 215000, 221000, 225000, 231000, 234000, 239000, 242000, 247000, 251000, 257000, 261000, 268000, 274000, 279000, 285000, 290000, 297000, 298000, 304000, 308000, 313000, 317000, 321000, 330000, 337000, 344000, 350000, 356000, 358000, 360000, 360000, 365000, 373000, 379000, 383000, 388000, 395000, 401000, 407000, 414000, 421000, 430000, 433000, 440000, 444000, 446000, 456000, 460000, 465000, 468000, 473000, 480000, 489000, 491000, 496000, 501000, 504000, 510000, 513000, 519000, 526000, 529000, 534000, 538000, 539000, 545000, 553000, 561000, 568000, 575000, 578000, 587000, 592000, 596000, 603000, 607000, 614000, 617000, 624000, 632000, 639000, 642000, 641000, 646000, 652000, 656000, 662000, 669000, 674000, 679000, 685000, 689000, 697000, 704000, 707000, 711000, 715000, 722000, 730000, 734000, 737000, 741000, 749000, 758000, 765000, 770000, 776000, 782000, 790000, 796000, 803000, 807000, 811000, 816000, 822000, 827000, 832000, 834000, 837000, 846000, 852000, 856000, 863000, 869000, 872000, 879000, 883000, 889000, 889000, 895000, 899000, 901000, 907000, 911000, 917000, 924000, 928000, 929000, 936000, 940000, 946000, 954000, 960000, 962000, 970000, 975000, 978000, 984000, 992000, 997000, 999000, 1006000, 1014000, 1018000, 1024000, 1028000, 1034000, 1040000, 1048000, 1052000, 1057000, 1062000, 1068000, 1073000, 1076000, 1083000, 1088000, 1092000, 1098000, 1107000, 1117000, 1123000, 1127000, 1131000, 1132000, 1138000, 1143000, 1152000, 1159000, 1164000, 1166000, 1174000, 1181000, 1185000, 1192000, 1199000, 1203000, 1206000, 1213000, 1221000, 1227000, 1229000, 1235000, 1237000, 1238000, 1242000, 1251000, 1255000, 1259000, 1262000, 1269000, 1277000, 1282000, 1289000, 1294000, 1298000, 1303000, 1309000, 1317000, 1321000, 1324000, 1331000, 1345000, 1349000, 1357000, 1365000, 1372000, 1381000, 1384000, 1388000, 1394000, 1397000, 1403000, 1407000, 1415000, 1423000, 1427000, 1433000, 1439000, 1447000, 1453000, 1456000, 1462000, 1467000, 1469000, 1475000, 1479000, 1487000, 1494000, 1499000, 1503000, 1507000, 1515000, 1520000, 1527000, 1534000, 1539000, 1545000, 1552000, 1559000, 1563000, 1568000, 1576000, 1582000, 1586000, 1594000, 1597000, 1604000, 1610000, 1614000, 1620000, 1625000, 1633000, 1638000, 1645000, 1650000, 1657000, 1662000, 1667000, 1673000, 1680000, 1687000, 1690000, 1694000, 1701000, 1709000, 1713000, 1718000, 1722000, 1728000, 1735000, 1737000, 1742000, 1749000, 1755000, 1767000, 1772000, 1777000, 1783000, 1790000, 1796000, 1801000, 1804000, 1811000, 1816000, 1826000, 1831000, 1835000, 1841000, 1847000, 1851000, 1854000, 1861000, 1868000, 1873000, 1878000, 1886000, 1891000, 1898000, 1898000, 1903000, 1912000, 1916000, 1918000, 1925000, 1930000, 1933000, 1938000, 1941000, 1943000, 1950000, 1954000, 1963000, 1967000, 1973000, 1979000, 1984000, 1990000, 1994000, 2002000, 2005000, 2009000, 2016000, 2022000, 2029000, 2035000, 2038000, 2044000, 2050000, 2054000, 2057000, 2059000, 2063000, 2067000, 2072000, 2081000, 2085000, 2090000, 2097000, 2105000, 2112000, 2117000, 2124000, 2130000, 2134000, 2140000, 2146000, 2148000, 2153000, 2157000, 2162000, 2166000, 2173000, 2181000, 2189000, 2195000, 2203000, 2210000, 2215000, 2219000, 2223000, 2227000, 2231000, 2243000, 2249000, 2256000, 2264000, 2268000, 2271000, 2273000, 2281000, 2285000, 2290000, 2299000, 2306000, 2308000, 2313000, 2318000, 2325000, 2325000, 2333000, 2340000, 2347000, 2350000, 2356000, 2361000, 2366000, 2369000, 2374000, 2382000, 2386000, 2394000, 2398000, 2400000, 2406000, 2410000, 2415000, 2420000, 2427000, 2431000, 2437000, 2439000, 2445000, 2449000, 2456000, 2459000, 2466000, 2471000, 2479000, 2485000, 2492000, 2499000, 2504000, 2511000, 2518000, 2521000, 2525000, 2528000, 2535000, 2542000, 2549000, 2552000, 2557000, 2563000, 2570000, 2575000, 2580000, 2586000, 2589000, 2596000, 2600000, 2603000, 2611000, 2616000, 2625000, 2633000, 2640000, 2646000, 2650000, 2656000, 2663000, 2666000, 2672000, 2678000, 2684000, 2689000, 2696000, 2697000, 2703000, 2710000, 2716000, 2723000, 2728000, 2733000, 2739000, 2746000, 2750000, 2754000, 2759000, 2764000, 2770000, 2775000, 2781000, 2785000, 2796000, 2802000, 2808000, 2816000, 2822000, 2828000, 2832000, 2837000, 2844000, 2852000, 2861000, 2866000, 2873000, 2876000, 2882000, 2884000, 2888000, 2894000, 2900000, 2903000, 2907000, 2912000, 2915000, 2921000, 2929000, 2933000, 2937000, 2945000, 2947000, 2953000, 2957000, 2961000, 2967000, 2972000, 2977000, 2983000, 2986000, 2994000, 3002000, 3015000, 3021000, 3025000, 3026000, 3031000, 3034000, 3040000, 3044000, 3050000, 3056000, 3060000, 3067000, 3069000, 3079000, 3084000, 3091000, 3095000, 3100000, 3106000, 3112000, 3120000, 3128000, 3131000, 3137000, 3143000, 3151000, 3159000, 3166000, 3166000, 3170000, 3176000, 3182000, 3189000, 3194000, 3201000, 3207000, 3217000, 3225000, 3233000, 3238000, 3244000, 3252000, 3261000, 3269000, 3277000, 3283000, 3290000, 3294000, 3300000, 3305000, 3307000, 3313000, 3319000, 3328000, 3335000, 3342000, 3347000, 3355000, 3360000, 3364000, 3368000, 3373000, 3377000, 3384000, 3392000, 3398000, 3405000, 3410000, 3414000, 3419000, 3427000, 3435000, 3440000, 3444000, 3452000, 3463000, 3469000, 3475000, 3481000, 3489000, 3495000, 3498000, 3503000, 3512000, 3520000, 3523000, 3531000, 3536000, 3542000, 3543000, 3549000, 3553000, 3558000, 3565000, 3569000, 3578000, 3585000, 3592000, 3602000]
