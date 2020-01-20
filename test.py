# 小女孩
face_landmarks_woman = face_landmarks_list[0]
browPoint_woman = util.getBrowPoint(face_landmarks_woman)

chin_woman = face_landmarks['chin']
leftPoint_woman, rightPoint_woman = util.getLeftRightPoint(chin_woman) # 计算的左右边界
left_woman = int(leftPoint_woman[0])
right_woman = int(rightPoint_woman[0])
newWidth_woman = right_woman - left_woman

# 高度按原来宽高的比例放缩
newHeight_woman = int(newWidth_woman / width_woman * height_woman)
# 下边界等于额头中心的Y轴点
bottom_woman = int(browPoint_woman[1])
# 上边界等于下边界减去高度
top_woman = bottom_woman - newHeight_woman