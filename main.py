from cocos.director import director


from cocos.scenes.sequences import SequenceScene

if __name__ == '__main__':
    director.init()

    from scene.levels_1_scene import level1_scene
    from scene.intro import intro_scene

    director.run(SequenceScene(intro_scene, level1_scene))

