<template>
  <div class="map-app">
    <!-- Header for time and current event -->
    <nav class="header">
      <div class="time">{{ currentTime }}</div>
      <div class="event">{{ currentEvent }}</div>
    </nav>

    <!-- Tabs for switching between maps -->
    <div class="tabs">
      <button 
        :class="{ active: activeTab === 'sports' }" 
        @click="activeTab = 'sports'"
      >
        體育館會場地圖
      </button>
      <button 
        :class="{ active: activeTab === 'building3' }" 
        @click="activeTab = 'building3'"
      >
        工三座位分配圖
      </button>
    </div>

    <!-- Tab content -->
    <div class="map-container">
      <div v-if="activeTab === 'sports'">
        <img src="@/assets/map1.png" alt="體育館會場地圖" class="map-image" />
      </div>
      <div v-if="activeTab === 'building3'">
        <img src="@/assets/map2.png" alt="工三座位分配圖" class="map-image" />
        <img src="@/assets/map3.png" alt="工三座位分配圖" class="map-image" />
        <img src="@/assets/map4.png" alt="工三座位分配圖" class="map-image" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'EventMap',
  data() {
    return {
      currentTime: '',
      currentEvent: '活動尚未開始', // 初始為活動尚未開始
      activeTab: 'sports', // 默認展示體育館會場地圖
      eventSchedule: {
        '10/19': [
          { start: '08:30', end: '09:00', event: '參賽者報到' },
          { start: '09:00', end: '10:30', event: '開幕式' },
          { start: '10:30', end: '12:00', event: 'Coding, 企業博覽會, 娛樂交流活動' },
          { start: '12:00', end: '13:30', event: '午餐' },
          { start: '13:30', end: '18:00', event: 'Coding, 企業博覽會, 娛樂交流活動' },
          { start: '18:00', end: '19:30', event: '晚餐' },
          { start: '19:30', end: '22:00', event: 'Coding, 娛樂交流活動' },
          { start: '22:00', end: '22:30', event: '宵夜' },
          { start: '22:30', end: '24:00', event: 'Coding, 參賽者休息' },
        ],
        '10/20': [
          { start: '00:00', end: '08:00', event: 'Coding, 參賽者休息' },
          { start: '08:00', end: '09:00', event: '早餐' },
          { start: '09:00', end: '11:00', event: 'Coding, 企業博覽會, 娛樂交流活動' },
          { start: '11:00', end: '11:50', event: '午餐, 活動攤位' },
          { start: '11:50', end: '15:10', event: '創客交流組決賽' },
          { start: '12:10', end: '14:00', event: '黑客組初賽' },
          { start: '15:20', end: '17:30', event: '黑客組決賽' },
          { start: '17:30', end: '18:30', event: '頒獎, 抽獎' },
          { start: '18:30', end: '19:30', event: '閉幕式' },
        ],
      },
    };
  },
    methods: {
      updateTime() {
        let now = new Date();
        now = new Date('2024-10-19T16:53:00');
        const day = `${now.getMonth() + 1}/${now.getDate()}`;
        this.currentTime = `${this.format24Hour(now)}`;

        this.currentTimeFlat = now.getHours() * 60 + now.getMinutes();

        this.updateCurrentEvent(day, this.currentTimeFlat);
      },

      format24Hour(date) {
        const hours = date.getHours().toString().padStart(2, '0');
        const minutes = date.getMinutes().toString().padStart(2, '0');
        return `${hours}:${minutes}`;
      },

      updateCurrentEvent(day, currentTimeFlat) {
        const schedule = this.eventSchedule[day];

        if (!schedule || (schedule && currentTimeFlat < 510)) {
          this.currentEvent = '活動尚未開始';
          return;
        }

        let eventFound = false;
        for (const event of schedule) {
          const [startHours, startMinutes] = event.start.split(':').map(Number);
          const [endHours, endMinutes] = event.end.split(':').map(Number);
          const eventStartFlat = startHours * 60 + startMinutes;
          const eventEndFlat = endHours * 60 + endMinutes;
          if (currentTimeFlat >= eventStartFlat && currentTimeFlat < eventEndFlat) {
            this.currentEvent = event.event;
            eventFound = true;
            break;
          }
        }

        if (!eventFound) {
          this.currentEvent = '活動已結束';
        }
      },
    },
  mounted() {
    // 每分鐘更新一次時間和活動
    this.updateTime();
    setInterval(this.updateTime, 10000);
  },
};
</script>

<style scoped>
.map-app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  text-align: center;
  margin: 20px auto;
  max-width: 800px;
  background-color: #f8f9fa;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.header {
  display: flex;
  justify-content: space-between;
  background-color: #333;
  color: white;
  padding: 10px;
  border-radius: 5px;
  margin-bottom: 20px;
}

.time {
  font-size: 18px;
  margin-right: 10px;
}

.event {
  font-size: 16px;
}

.tabs {
  display: flex;
  justify-content: center;
  margin-bottom: 20px;
}

.tabs button {
  background-color: #ddd;
  border: none;
  padding: 10px 20px;
  margin: 0 5px;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

.tabs button.active {
  background-color: #333;
  color: white;
}

.map-container {
  margin-top: 20px;
}

.map-image {
  width: 100%;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}
</style>
