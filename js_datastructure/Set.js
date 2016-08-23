function Set() {
  var items = {};

  this.has = function(value){
    return items.hasOwnProperty(value);
  };
  this.add = function(value){
    if (!this.has(value)) {
      // 添加一个值的时候，把它同时作为键和值保存，便于查找
      items[value] = value;
      return true;
    } else {
      return false;
    }
  };
  this.remove = function(value){
    if (this.has(value)) {
      delete items[value];
      return true;
    } else {
      return false;
    }
  };
  this.clear = function(){
    items = {};
  };
  this.size = function(){
    var count = 0;
    for(var prop in items){
      if (items.hasOwnProperty(prop)) {
        ++count;
      }
    }
  }
}