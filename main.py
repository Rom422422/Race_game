from cpe3d import Camera
from viewerGL import ViewerGL

# import audio, Pydub

def main():

    viewer = ViewerGL()

    viewer.set_camera(Camera())
    viewer.cam.transformation.translation.y = 3
    viewer.cam.transformation.rotation_center = viewer.cam.transformation.translation.copy()

    viewer.generate_track()
    viewer.run()


if __name__ == '__main__':
    main()
