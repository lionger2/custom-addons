layui.extend({
    setter: 'config',
    admin: 'admin',
}).define(['setter', 'admin'], function(exports) {
    if (layui.admin.screen() < 2){
        layui.admin.sideFlexible(null);
    }else {
        layui.admin.sideFlexible('spread');
    }
    exports('index', {});
});