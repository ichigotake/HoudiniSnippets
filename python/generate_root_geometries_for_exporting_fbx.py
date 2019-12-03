# Sinopsys
# 
#   >>> hou.session.generate_exporting_nodes(hou.node('/'))
# 
# Description
# 
# ノードを指定し、FBXエクスポート用のノードを新たに生成します。
# 1. 指定したノードからノード名 `OUT_$name` を探索する
# 2. /objに新しいGeomeryノードを、名前 `$name` で作成する
#   - 中身は OUT_$name` を参照する Object Mergeノード一つ
# 
# Known issues
# - HDAの中まで探索してしまう
def generate_exporting_nodes(node):
    for child in node.children():
        if child.name().startswith("OUT") :
            if child.name() != 'OUT':
                name = child.name().replace('OUT_', '').lower()
                if not hou.node('/obj/' + name):
                    print name
                    g = hou.node('/obj').createNode('geo', name)
                    # エクスポート時にしか使わないノードだからいらない気がする
                    # まとめて消せるように、移動させない方がよさそう
                    #g.moveToGoodPosition()
                    om = g.createNode('object_merge', 'object_merge')
                    om.parm('objpath1').set(om.relativePathTo(child))
        generate_exporting_nodes(child)
