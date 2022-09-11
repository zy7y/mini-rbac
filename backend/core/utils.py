def list_to_tree(
    menus, parent_flag: str = "pid", children_key: str = "children"
) -> list:
    """
    list 结构转 树结构
    :param menus: [{id:1, pid: 3}]
    :param parent_flag: 节点关系字段
    :param children_key: 生成树结构的子节点字段
    :return: list 类型的 树嵌套数据
    """ ""
    # 先转成字典 id作为key, 数据作为value
    menu_map = {menu["id"]: menu for menu in menus}
    arr = []
    for menu in menus:

        # 有父级
        if mid := menu.get(parent_flag):
            # 有 子项的情况
            if result := menu_map[mid].get(children_key):
                result.append(menu)
            else:
                # 无子项的情况
                menu_map[mid][children_key] = [menu]
        else:
            arr.append(menu)
    return arr


def menu_table():
    """生成菜单表数据"""
    from models import MenuModel
    MenuModel.bulk_create([
        MenuModel(name="系统管理",
                  meta={"icon": "Grid"},
                  path="/system",
                  type=0),
        MenuModel(name="系统设置",
                  meta={"icon": "Setting"},
                  path="/setting",
                  type=0),
        MenuModel(name="菜单管理",
                  meta={"icon": "Menu"},
                  path="/system/menu",
                  type=1,
                  component="/system/menu",
                  pid=1,
                  api="/menu",
                  method="{'GET}",
                  regx="^/menu$"
                  )
    ])