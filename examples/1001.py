# 导入相关库
import sensor, image, lcd, time
import KPU as kpu
# 液晶屏初始化
lcd.init()
#摄像头初始化
sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.set_vflip(1)
sensor.set_hmirror(1)
sensor.run(1)
# 开机加载模型的labels
lcd.clear()
lcd.draw_string(100,96,"MobileNet Demo")
lcd.draw_string(100,112,"Loading labels...")
# 这里打开的是flash里的labels.txt，如果我们选择打开sd卡中的文件，路径为：“labels.txt”
f=open('labels.txt','r')
labels=f.readlines()
f.close()
# 加载1000中物体分类模型
task = kpu.load(0x300000) 
clock = time.clock()

while(True):
    img = sensor.snapshot()
    clock.tick()
    fmap = kpu.forward(task, img)
    fps=clock.fps()
    # 这里把运行的结果转换成了一个list对象，然后找到了最大值的下标， 
    plist=fmap[:]
    pmax=max(plist) 
    max_index=plist.index(pmax) 
    a = lcd.display(img, oft=(0,0))
    # 通过这个下标我们就知道标签名是什么了（labels[max_index]）
    lcd.draw_string(0, 0, "%.2f:%s                            "%(pmax, labels[max_index].strip()))
    print(fps)
a = kpu.deinit(task)
