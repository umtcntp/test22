import cartopy.crs as ccrs
import matplotlib.pyplot as plt
# PlateCarree projeksiyonu ile yeni bir eksen oluşturma
ax = plt.axes(projection=ccrs.PlateCarree())

# Grafiğe standart bir dünya haritası görseli ekleme
ax.stock_img()

# New York ve Delhi şehirlerinin koordinatlarını ayarlama
ny_lon, ny_lat = -75, 43
delhi_lon, delhi_lat = 77.23, 28.61

# New York ve Delhi arasındaki rotayı temsil eden bir çizgi çizme
plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='red', linewidth=2, marker='o',
         transform=ccrs.Geodetic(),  # Koordinatları dönüştürmek için jeodezik projeksiyon kullanma
         )

# New York ve Delhi şehirleri arasında kesikli bir çizgi çizme
plt.plot([ny_lon, delhi_lon], [ny_lat, delhi_lat],
         color='gray', linestyle='--',
         transform=ccrs.PlateCarree(),  # Koordinatları dönüştürmek için PlateCarree projeksiyonunu kullanma
         )

# New York'un koordinatlarına sahip noktaya "New York" yazısını ekleme
plt.text(ny_lon - 3, ny_lat - 12, 'New York',
         horizontalalignment='right',  # Yatay metin hizalamasını ayarlama
         transform=ccrs.Geodetic()  # Koordinatları dönüştürmek için jeodezik projeksiyon kullan
         )

# Delhi'nin koordinatlarına sahip noktaya "Delhi" yazısını ekleme
plt.text(delhi_lon + 3, delhi_lat - 12, 'Delhi',
         horizontalalignment='left',  # Yatay metin hizalaması
         transform=ccrs.Geodetic()  # Koordinatları dönüştürmek için jeodezik projeksiyon kullanma
         )

# Harita grafiğini gösterme
plt.show()