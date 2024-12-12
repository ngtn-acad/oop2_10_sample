async function getRestaurantFeatures() {
  const points = await fetch("/api/restaurants")
    .then((res) => res.json())
    .catch((err) => {
      console.error(err);
      return [];
    });
  const features = [];
  points.map((point) =>
    features.push({
      type: "Feature",
      properties: {
        P27_005: point.name,
        P27_006: point.address,
      },
      geometry: {
        type: "Point",
        coordinates: [point.long, point.lat],
      },
    })
  );
  return features;
}

let features = [];
getRestaurantFeatures().then((res) => {
  features = res;
});

const map = new maplibregl.Map({
  container: "map",
  center: [137.111893, 35.184185], // 中心座標
  maxPitch: 85, // 最大の傾き、デフォルトは60
  zoom: 14, // ズームレベル
  style: {
    // スタイル仕様のバージョン番号。8を指定する
    version: 8,
    // データソース
    sources: {
      // 背景地図 OpenStreetMapのラスタタイル
      "background-osm-raster": {
        // ソースの種類。vector、raster、raster-dem、geojson、image、video のいずれか
        type: "raster",
        // タイルソースのURL
        tiles: ["https://tile.openstreetmap.jp/styles/osm-bright-ja/{z}/{x}/{y}.png"],
        // タイルの解像度。単位はピクセル、デフォルトは512
        tileSize: 256,
        // データの帰属
        attribution:
          "<a href='https://www.openstreetmap.org/copyright' target='_blank'>© OpenStreetMap contributors</a>",
      },
    },
    // 表示するレイヤ
    layers: [
      // 背景地図としてOpenStreetMapのラスタタイルを追加
      {
        // 一意のレイヤID
        id: "background-osm-raster",
        // レイヤの種類。background、fill、line、symbol、raster、circle、fill-extrusion、heatmap、hillshade のいずれか
        type: "raster",
        // データソースの指定
        source: "background-osm-raster",
      },
    ],
  },
});

map.on("load", async () => {
  const iconImage = await map.loadImage("./static/icon.png");
  map.addImage("restaurant_icon", iconImage.data);
  map.addSource("restaurant_point", {
    type: "geojson",
    data: {
      type: "FeatureCollection",
      name: "point",
      crs: { type: "name", properties: { name: "urn:ogc:def:crs:OGC:1.3:CRS84" } },
      features: features,
    },
  });
  map.addLayer({
    id: "restaurant_point",
    type: "symbol",
    source: "restaurant_point",
    layout: {
      "icon-image": "restaurant_icon",
      "icon-size": 0.1,
    },
  });
});

map.on("click", "restaurant_point", (e) => {
  var coordinates = e.features[0].geometry.coordinates.slice();
  var name = `<strong>${e.features[0].properties.P27_005}</strong><p>${e.features[0].properties.P27_006}</p>`;

  while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
    coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
  }
  // ポップアップを表示する
  new maplibregl.Popup({
    offset: 10, // ポップアップの位置
    closeButton: false, // 閉じるボタンの表示
  })
    .setLngLat(coordinates)
    .setHTML(name)
    .addTo(map);
});
