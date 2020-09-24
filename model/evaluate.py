import numpy as np
from numpy import (array, dot, arccos, clip)
from numpy.linalg import norm


def get_distance(point1,point2):
	x1,y1= point1[0],point1[1]
	x2,y2= point2[0],point2[1]
	# Euclidean distance shorter way(from scipy.spatial import distance, distance.euclidean)
	return ((x1-x2)**2 + (y1-y2)**2)**0.5

def sameLine(points):
    x0,y0  = points[0]
    points = [ (x,y) for x,y in points if x != x0 or y != y0 ]      # Other points
    slopes = [ (y-y0)/(x-x0) if x!=x0 else None for x,y in points ] # None for vertical Line
    #print(slopes)
    return all( s == slopes[0] for s in slopes)
	
def get_angle(u,v):
	c=dot(u,v)/norm(u)/norm(v) # -> cosine of the angle
	angle = arccos(clip(c, -1, 1))
	return np.degrees(angle)
	
def warrior_ii(get_coordinates):
	##right
	feedback=''
	try:
		x1,y1=get_coordinates['RHip']
		x2,y2=get_coordinates['RKnee']
		x3,y3=get_coordinates['RAnkle']
		#print("Right coord")
		#print(x1,y1,x2,y2,x3,y3)
		##left
		x4,y4= get_coordinates['LHip']
		x5,y5= get_coordinates['LKnee']
		x6,y6= get_coordinates['LAnkle']
		#print(x4,y4,x5,y5,x6,y6)
		if sameLine([(x1,y1),(x2,y2),(x3,y3)]):
			feedback+=("Good Job! Your right side is in a nice straight form.")
		else:
			feedback+=("Try Straightening your right hip and right knee so they are in a straight line.")
		vec1=[(x5-x4),(y5-y4)]
		vec2=[(x6-x5),(y6-y5)]
		#print(vec1,vec2)
		angle=get_angle(vec1,vec2)
		#print(angle)
		if angle<90 and angle>=75:
			feedback+=("Almost there. Try bending your knee outward so it is stacked on top of your ankle.")
		elif angle==90 or angle==95 or angle==85:
			feedback+="Excellent. Warrior 2 pose perfectly done."
		elif angle>90 and angle<115:
			feedback+=("Almost there. Try bending your knee outward so it is stacked on top of your ankle. Knee should not go beyond your toes")
		else:
			feedback+=("Incorrect posture. Stack your left knee on top of your ankle and creating a right angle with your hip.")
		
	except:
		feedback+=("Could not detect all keypoints.Upload a clearer picture and please make sure your clothes don't blend into the background :)")
	return feedback

def goddess(get_coordinates):
	feedback=''

	try:
		xrh,yrh=get_coordinates['RHip']
		xrk,yrk=get_coordinates['RKnee']
		xra,yra=get_coordinates['RAnkle']
		xlh,ylh=get_coordinates['LHip']
		xlk,ylk=get_coordinates['LKnee']
		xla,yla=get_coordinates['LAnkle']
		'''print("RHIP",xrh,yrh)
						print("rknee",xrk,yrk)
						print("lHIP",xlh,ylh)
						print("lknee",xlk,ylk)
						print(xlh,xlk,ylh,ylk)'''
		hip_to_knee_r=[(xrh-xrk),(yrh-yrk)]
		hip_to_knee_l=[(xlh-xlk),(ylh-ylk)]
		#print(hip_to_knee_r,hip_to_knee_l)
		angle_between_legs = get_angle(hip_to_knee_r,hip_to_knee_l)
		#print(angle_between_legs)

		if angle_between_legs>160:
			feedback+="Great Job. Your thighs are parallel to the ground. The form is great."
		else:
			feedback+="Almost there. Keep pushing downwards so that your legs are parallel to the ground and your thighs are stretched."
		###Angles between legs should be right angles

		right_ankle_knee=[(xra-xrk),(yra-yrk)]
		left_ankle_knee=[(xla-xlk),(yla-ylk)]

		rightleg_angle=get_angle(right_ankle_knee,hip_to_knee_r)
		leftleg_angle=get_angle(left_ankle_knee,hip_to_knee_l)

		if rightleg_angle>90 and rightleg_angle<=110:
			feedback+="Correct Positioning of the right leg. A nice right angle is formed."
		elif rightleg_angle<90:
			feedback+='Push your right knee outwards such that it is stacked directly on top of the right ankle.Do not forget to keep your thighs parallel to the ground.'
		else:
			feedback+='Push your right knee inwards such that it is stacked directly on top of the right ankle.Do not forget to keep your thighs parallel to the ground.'

		if leftleg_angle>90 and leftleg_angle<=110:
			feedback+="Correct Positioning of the left leg. A nice right angle is formed."
		elif leftleg_angle<90:
			feedback+='Push your left knee outwards such that it is stacked directly on top of the left ankle.Do not forget to keep your thighs parallel to the ground.'
		else:
			feedback+='Push your left knee inwards such that it is stacked directly on top of the left ankle.Do not forget to keep your thighs parallel to the ground.'

	except:
		feedback+=("Could not detect all keypoints.Upload a clearer picture and please make sure your clothes don't blend into the background :)")
	return feedback
	
def shouldershrug(bef_points,aft_points):
	feedback=''
	try:
		try:
			xra,yra=aft_points['RAnkle']
			xla,yla=aft_points['LAnkle']
			xls,yls=aft_points['LShoulder']
			xrs,yrs=aft_points['RShoulder']

			shoulder_dis=get_distance([xls,yls],[xrs,yrs])
			feet_dis=get_distance([xra,yra],[xla,yla])

			if  (shoulder_dis + 20 <= feet_dis <= shoulder_dis-20) or (feet_dis + 20 <= shoulder_dis <= feet_dis-20):
				feedback+='Great going. Your shoulder width and distance between your feet is almost the same. Do not have a wider or a more narrow stance.'
			elif shoulder_dis<feet_dis:
				feedback+=' Your feet should be shoulder width apart. Try bringing them closer.'
			elif shoulder_dis>feet_dis:
				feedback+='Your feet must be shoulder width apart. Try having a wider stance and stacking your knees below your shoulders.'
		except:
			feedback+='Could not detect lower body keypoints.'
		#print(shoulder_dis,feet_dis)

		xrear,yrear=bef_points['REar']
		xrs,yrs=bef_points['RShoulder']
		before_right=get_distance([xrear,yrear],[xrs,yrs])
		xlear,ylear=bef_points['LEar']
		xls,yls=bef_points['LShoulder']
		before_left=get_distance([xlear,ylear],[xls,yls])

		xrear,yrear=aft_points['REar']
		xrs,yrs=aft_points['RShoulder']
		after_right=get_distance([xrear,yrear],[xrs,yrs])
		xlear,ylear=aft_points['LEar']
		xls,yls=aft_points['LShoulder']
		after_left=get_distance([xlear,ylear],[xls,yls])

		'''print(before_left,after_left)
		print(before_right,after_right)'''

		if before_left/2 - 20 <= after_left <= before_left/2 +20:
			feedback+='Good form on the left. Your left shoulder is nicely shrugged all the way up to your left ear.'
		else:
			feedback+='Your shoulder does not go through enough motion. Shrug it harder.'

		if before_right/2 - 20 <= after_right <= before_right/2 +20:
			feedback+='Good form on the right. Your right shoulder is nicely shrugged all the way up to your right ear.'
		else:
			feedback+='Your shoulder does not go through enough motion. Shrug it harder.'
	except:
		feedback+=("Could not detect all keypoints.Upload a clearer picture and please make sure your clothes don't blend into the background :)")

	return feedback






