cd ~/odoo-dev/anodoo

(将relation批量替换为新模块)

mkdir anodoo_relation;
\cp -r -a ../custom-addons/siwei_module_template/* anodoo_relation;   

mv anodoo_relation/controllers/oppor_controllers.py anodoo_relation/controllers/relation_controllers.py;
mv anodoo_relation/data/oppor_data.xml anodoo_relation/data/relation_data.xml;
mv anodoo_relation/demo/oppor_demo.xml anodoo_relation/demo/relation_demo.xml;
mv anodoo_relation/models/oppor_models.py anodoo_relation/models/relation_models.py;
mv anodoo_relation/security/oppor_security.xml anodoo_relation/security/relation_security.xml;
mv anodoo_relation/views/oppor_menu.xml anodoo_relation/views/relation_menu.xml;
mv anodoo_relation/views/oppor_templates.xml anodoo_relation/views/relation_templates.xml;
mv anodoo_relation/views/oppor_views.xml anodoo_relation/views/relation_views.xml;

进入eclipse, 刷新, 选择模块, 在当前resource中, 批量替换oppor 为 relation  应该有9个地方
修改mani文件

