var graph = new Springy.Graph();

var valentino = graph.newNode({
  label: 'Valentino Volpato',
  ondoubleclick: function() { alert("Hello!"); }
});
var dante = graph.newNode({label: 'Dante Volpato'});
var valentina = graph.newNode({label: 'Valentina'});
var tiago = graph.newNode({label: 'Tiago'});
var henrique = graph.newNode({label: 'Henrique'});

graph.newEdge(valentino, dante, {color: '#7DBE3C'});
graph.newEdge(dante, valentina, {color: '#7DBE3C'});
graph.newEdge(valentina, tiago, {color: '#7DBE3C'});
graph.newEdge(valentina, henrique, {color: '#7DBE3C'});

jQuery(function(){
  var springy = window.springy = jQuery('#arvore_familia').springy({
    graph: graph,
    nodeSelected: function(node){
      console.log('Node selected: ' + JSON.stringify(node.data));
    }
  });
});
