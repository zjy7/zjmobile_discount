
import sys
import pyautogui
from base64 import b64decode
from io import BytesIO
from PIL import Image
from gui_head import IMAGE_GUI
from runAsAdmin import RunAsAdmin
print("1111")
def hello():
    print("hello world!", flush=True)
    im = pyautogui.screenshot()
    # im.save('screenshot.png')

    # way = pyautogui.confirm('领导，要走哪条路？', buttons=['农村路', '水路', 'lulu'])
    # print(way)
    # isEqualLL = way == 'lulu'
    # print(isEqualLL)

    # alert = pyautogui.alert(text='警告！敌军来袭.', title='这个是警告框')
    # print(alert)
    # print(alert == 'OK') #True

    # password = pyautogui.password('请输入密码')
    # print(password)

    # input = pyautogui.prompt('请输入指令：')
    # print(input)

    IMAGE_GUI = """
iVBORw0KGgoAAAANSUhEUgAAABoAAAAZCAYAAAAv3j5gAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAO2SURBVEhLfVZbS5RRFPUtCHqM8AqBhY6ak1NE0HwzCmJll6kUEyqpsELTiki6/oYieokIMaiHogeLKIhC6CEoy4mpJIWcm3jN/Ae7b+3T+r7zqfiw2OfsM7PWWfvsc2YKikMx2Ro7LOFoQrY1tEpd/Igi7BySSH2LB3zGwKzXxVsUkfpWzZm8yQGYl1TVeygoqYq7C0c8MgjYYhTAnBHkIAs7RpgiiFxDLKqM+UJFlY63e5LbYrZLfgawyZcKYo4IgeJQ3BfilynASDc2IIYyg4hCdoQIywmR0uoGI4QzIjkABx6h5YxC5rNmx7YTu5yImEMEYiihnhHPh+Rmx4acm+C6L+w7oYOlYhDgORWUVtcHOo7kQGS36+hos+zt75bojXYJJ5rd9USAHIQEcnSJOdwQ6sjeLWKtc0CaX/ZK25+bcvTvrQBas9dlR09boEQkDkdRfpNHDk4AlFAdBZ0ckqYvl2XfzDVpdoFI2PPtfW1K6JXLFbEdIl9Y4XhiBWU1DSrCc9j5oFPi+T5F2f39Enp1TMex3BUputMktUOndO5k+6S26aCS2y60fK4oIgS8ZmB7Q0RdjVyQbenLis1vO6T601lvXu6Kbkl26XhX+qo4fSeVnKA7FXPFKaKOlr4MFb96pXL8wooIjV+Uq7lHMvJnTBYXFxWZbF76Hz+XOsfcLYpCiGVTIdwjdB0dbXx3VspGe1bEwOR7WVhYWBE/RsckEsO9M2cEMbjxSgdHvJiI5Z0JWZ/qWoa28bsyPz8v09PTMjAwILlcTueDg4OSTCZ1/PzFG88NxHhhA6XT8/kfS+53yLrkuQDupV/L3NyczM7OyvDwsMzMzOg8lUpJNpvVcSab85qBQhDx7hHPh2cFrB06LWs+d8qaL2cUt3+/UvLVMJHOqBuI2V2n94iO8DKwxWsbErLh7gmpie6XmsaEbGraK4nu8zI1NbUqnjx7oaVj9y0Tst3wvJAD6BZ4+OipTE5Orojhr99kq9t55lH2nyA2hN4jLJKQkYIAnQLHOy/J0IePkslkJZ/PS+r7T5mYSEvjweNKjtLRFR0tawZbiA45JkgSccfb9SFukV2728XZ065rPCPeI88RSwfQhV0uAjnjzIhBALDHNpCnGz2jwoqou2DIzY59N4h2Cblm8hj7QtwAgRyfH690utv/P3YARQyh+T9huzJr5k1jhzHawsteb37ZlMbfNca2w+AGsOZHkFPA/Iiargs4IimjTUg33IwhNdHcPVNCOLIFscbSFYfi8g9ffQl1VgATggAAAABJRU5ErkJggg==
    """

    # 检测是否有看视频的标题图像，起始xy坐标和宽高
    base64_image = IMAGE_GUI
    image_data = b64decode(base64_image)
    image = Image.open(BytesIO(image_data))
    # image.show()

    wx1 = pyautogui.locateOnScreen(image, confidence=0.9)
    wxall = pyautogui.locateAllOnScreen(image, confidence=0.9)

    print('into 222')
    print(wx1)
    print(wxall)

    ll = list(wxall)
    print(ll)
    # print(ll.length)
    print(ll[0])
    print(ll[0].left)

    # for x in wxall:
    #     print(x)

    print('---------------------')
    currentP = pyautogui.position()
    print(currentP)

    currentSize = pyautogui.size()
    print(currentSize)

    isonscreen = pyautogui.onScreen(3000,100)
    print(isonscreen)

    pyautogui.PAUSE = 2.5

    print(pyautogui.FAILSAFE)

    # pyautogui.moveTo(wx1.left, wx1.top)

    # pyautogui.click(wx1.left + 10, wx1.top + 10, button='left')

    # pyautogui.moveTo(2164, 888, duration = 1)
    # pyautogui.dragTo(2164, 588, duration = 1)

    print(pyautogui.KEYBOARD_KEYS)

    wx2 = pyautogui.locateOnScreen('wx_small.png', confidence=0.9)
    print(wx2)

    wxminitop = pyautogui.locateOnScreen('wx_mini_top.png', confidence=0.9)
    print(wxminitop)
    print(wxminitop == None)
    if wxminitop:
        print('找到了这张图片')
        print(wxminitop)
        print(wxminitop.left)
        print(wxminitop.top)
        print(wxminitop.width)
        print(wxminitop.height)
    else:
        print('没找到小程序的图片')

    sys.stdout.flush()

hello()