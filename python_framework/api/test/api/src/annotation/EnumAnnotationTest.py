import time
from python_helper import log, Test, SettingHelper, RandomHelper
from python_framework import Enum, EnumItem
from python_framework import HttpStatus, ActuatorHealthStatus

LOG_HELPER_SETTINGS = {
    log.LOG : False,
    log.SUCCESS : True,
    log.SETTING : True,
    log.DEBUG : True,
    log.WARNING : True,
    log.WRAPPER : True,
    log.FAILURE : True,
    log.ERROR : True,
    log.TEST : False
}

@Test(environmentVariables={
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    }
)
def enum_withSuccess() :
    TEST_ITERATION = 1
    ASSERT_ITERATION = 1
    discount = 0
    instanciationTime = 0
    equalTestTime = 0
    start = time.time()
    for _ in range(TEST_ITERATION) :
        # arrange
        discountStart = time.time()
        ITS_NAME = RandomHelper.string(minimum=5, maximum=10)
        A_NAME = RandomHelper.string(minimum=5, maximum=10)
        TEST_NAME = RandomHelper.string(minimum=5, maximum=10)
        ITS_LABEL = RandomHelper.string(minimum=5, maximum=10)
        A_LABEL = RandomHelper.string(minimum=5, maximum=10)
        TEST_LABEL = RandomHelper.string(minimum=5, maximum=10)
        ITS_NUMERIC = RandomHelper.integer(minimum=5, maximum=1000)
        A_NUMERIC = RandomHelper.integer(minimum=5, maximum=1000)
        TEST_NUMERIC = RandomHelper.integer(minimum=5, maximum=1000)
        ITS_VALUE = 'ITS'
        A_VALUE = 'A'
        TEST_VALUE = 'TEST'
        discount += time.time() - discountStart

        # act
        discountStart = time.time()
        @Enum()
        class MyEnumTest :
            ITS = EnumItem(name=ITS_NAME, label=ITS_LABEL, numeric=ITS_NUMERIC)
            A = EnumItem(name=A_NAME, label=A_LABEL, numeric=A_NUMERIC)
            TEST = EnumItem(name=TEST_NAME, label=TEST_LABEL, numeric=TEST_NUMERIC)
        discount += time.time() - discountStart
        instanciationTimeInit = time.time()
        MY_ENUM_TEST = MyEnumTest()
        instanciationTime += time.time() - instanciationTimeInit

        # assert
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert ITS_VALUE == MY_ENUM_TEST.ITS
        discountStart = time.time()
        log.log(enum_withSuccess, f'ITS_VALUE == MY_ENUM_TEST.ITS assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert A_VALUE == MY_ENUM_TEST.A
        discountStart = time.time()
        log.log(enum_withSuccess, f'A_VALUE == MY_ENUM_TEST.A assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert TEST_VALUE == MY_ENUM_TEST.TEST
        discountStart = time.time()
        log.log(enum_withSuccess, f'TEST_VALUE == MY_ENUM_TEST.TEST assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert ITS_NAME == MY_ENUM_TEST.ITS.name
        discountStart = time.time()
        log.log(enum_withSuccess, f'ITS_NAME == MY_ENUM_TEST.ITS.name assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert A_NAME == MY_ENUM_TEST.A.name
        discountStart = time.time()
        log.log(enum_withSuccess, f'A_NAME == MY_ENUM_TEST.A.name assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert TEST_NAME == MY_ENUM_TEST.TEST.name
        discountStart = time.time()
        log.log(enum_withSuccess, f'TEST_NAME == MY_ENUM_TEST.TEST.name assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert ITS_LABEL == MY_ENUM_TEST.ITS.label
        discountStart = time.time()
        log.log(enum_withSuccess, f'ITS_LABEL == MY_ENUM_TEST.ITS.label assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert A_LABEL == MY_ENUM_TEST.A.label
        discountStart = time.time()
        log.log(enum_withSuccess, f'A_LABEL == MY_ENUM_TEST.A.label assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert TEST_LABEL == MY_ENUM_TEST.TEST.label
        discountStart = time.time()
        log.log(enum_withSuccess, f'TEST_LABEL == MY_ENUM_TEST.TEST.label assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert ITS_NUMERIC == MY_ENUM_TEST.ITS.numeric
        discountStart = time.time()
        log.log(enum_withSuccess, f'ITS_NUMERIC == MY_ENUM_TEST.ITS.numeric assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert A_NUMERIC == MY_ENUM_TEST.A.numeric
        discountStart = time.time()
        log.log(enum_withSuccess, f'A_NUMERIC == MY_ENUM_TEST.A.numeric assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert TEST_NUMERIC == MY_ENUM_TEST.TEST.numeric
        discountStart = time.time()
        log.log(enum_withSuccess, f'TEST_NUMERIC == MY_ENUM_TEST.TEST.numeric assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert MyEnumTest.map(MY_ENUM_TEST.ITS.enumValue) == MY_ENUM_TEST.ITS
        discountStart = time.time()
        log.log(enum_withSuccess, f'MyEnumTest.map(MY_ENUM_TEST.ITS.enumValue) == MY_ENUM_TEST.ITS assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert MyEnumTest.map(MY_ENUM_TEST.A.enumValue) == MY_ENUM_TEST.A
        discountStart = time.time()
        log.log(enum_withSuccess, f'MyEnumTest.map(MY_ENUM_TEST.A.enumValue) == MY_ENUM_TEST.A assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert MyEnumTest.map(MY_ENUM_TEST.TEST.enumValue) == MY_ENUM_TEST.TEST
        discountStart = time.time()
        log.log(enum_withSuccess, f'MyEnumTest.map(MY_ENUM_TEST.TEST.enumValue) == MY_ENUM_TEST.TEST assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert MY_ENUM_TEST.ITS.enumValue.enum == MY_ENUM_TEST
        discountStart = time.time()
        log.log(enum_withSuccess, f'MY_ENUM_TEST.ITS.enumValue.enum == MY_ENUM_TEST assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert MY_ENUM_TEST.A.enumValue.enum == MY_ENUM_TEST
        discountStart = time.time()
        log.log(enum_withSuccess, f'MY_ENUM_TEST.A.enumValue.enum == MY_ENUM_TEST assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert MY_ENUM_TEST.TEST.enumValue.enum == MY_ENUM_TEST
        discountStart = time.time()
        log.log(enum_withSuccess, f'MY_ENUM_TEST.TEST.enumValue.enum == MY_ENUM_TEST assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert not MY_ENUM_TEST.ITS.enumValue.enum == MyEnumTest
        discountStart = time.time()
        log.log(enum_withSuccess, f'not MY_ENUM_TEST.ITS.enumValue.enum == MyEnumTest assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert not MY_ENUM_TEST.A.enumValue.enum == MyEnumTest
        discountStart = time.time()
        log.log(enum_withSuccess, f'not MY_ENUM_TEST.A.enumValue.enum == MyEnumTest assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert not MY_ENUM_TEST.TEST.enumValue.enum == MyEnumTest
        discountStart = time.time()
        log.log(enum_withSuccess, f'not MY_ENUM_TEST.TEST.enumValue.enum == MyEnumTest assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        equalTestTimeStart = time.time()
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert MY_ENUM_TEST.ITS.enumValue.enum == MyEnumTest()
        discountStart = time.time()
        log.log(enum_withSuccess, f'MY_ENUM_TEST.ITS.enumValue.enum == MyEnumTest() assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert MY_ENUM_TEST.A.enumValue.enum == MyEnumTest()
        discountStart = time.time()
        log.log(enum_withSuccess, f'MY_ENUM_TEST.A.enumValue.enum == MyEnumTest() assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        timeAssertInit = time.time()
        for _ in range(ASSERT_ITERATION) :
            assert MY_ENUM_TEST.TEST.enumValue.enum == MyEnumTest()
        discountStart = time.time()
        log.log(enum_withSuccess, f'MY_ENUM_TEST.TEST.enumValue.enum == MyEnumTest() assert duration: {time.time() - timeAssertInit}')
        discount += time.time() - discountStart
        assert MyEnumTest() == MyEnumTest()
        equalTestTime += (time.time() - equalTestTimeStart)

    log.debug(enum_withSuccess, f'discount time: {discount}')
    log.debug(enum_withSuccess, f'3 * equal evaluation time : {equalTestTime}')
    log.debug(enum_withSuccess, f'instanciation time : {instanciationTime}')
    log.debug(enum_withSuccess, f'test duration: {time.time() - start - equalTestTime - discount}')


# LOG_HELPER_SETTINGS = {
#     log.LOG : True,
#     log.SUCCESS : True,
#     log.SETTING : True,
#     log.DEBUG : True,
#     log.WARNING : True,
#     log.WRAPPER : True,
#     log.FAILURE : True,
#     log.ERROR : True,
#     log.TEST : True
# }
@Test(environmentVariables={
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    }
)
def otherEnum_withSuccess() :
    @Enum(associateReturnsTo='value', instanceLog=True)
    class MyOtherEnumTest :
        ONE = EnumItem(value=1)
        TWO = EnumItem(value=2)
        THREE = EnumItem(value=3)
    @Enum(associateReturnsTo='value', instanceLog=False)
    class MyThirdEnumTest :
        ONE = EnumItem(value=4)
        TWO = EnumItem(value=5)
        THREE = EnumItem(value=6)

    # act
    one = MyOtherEnumTest().ONE
    anotherOne = MyThirdEnumTest().ONE

    # assert
    assert one == 1
    assert anotherOne == 4
    assert MyOtherEnumTest() != MyThirdEnumTest()
    assert MyOtherEnumTest() == MyOtherEnumTest()
    assert MyOtherEnumTest().ONE == MyOtherEnumTest().ONE
    assert MyOtherEnumTest().TWO != MyOtherEnumTest().ONE
    assert 8 == MyOtherEnumTest().TWO + MyThirdEnumTest().THREE

@Test(environmentVariables={
        SettingHelper.ACTIVE_ENVIRONMENT : SettingHelper.LOCAL_ENVIRONMENT,
        **LOG_HELPER_SETTINGS
    }
)
def python_framework_status() :
    # arrange
    # act
    # assert
    assert 200 == HttpStatus.OK
    assert 'UP' == ActuatorHealthStatus.UP