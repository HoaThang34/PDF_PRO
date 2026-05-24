const features = [
  {
    title: 'AI-powered tools',
    desc: 'Ứng dụng trí tuệ nhân tạo để nhận dạng văn bản, tối ưu hình ảnh và xử lý PDF thông minh.',
    icon: '🤖',
  },
  {
    title: 'Cloud sync',
    desc: 'Đồng bộ dữ liệu lên đám mây, truy cập mọi lúc mọi nơi trên mọi thiết bị.',
    icon: '☁️',
  },
  {
    title: 'Real-time editing',
    desc: 'Chỉnh sửa PDF trực tiếp trong thời gian thực, không cần chờ đợi hay tải lên lại.',
    icon: '⚡',
  },
  {
    title: 'Batch processing',
    desc: 'Xử lý hàng loạt file cùng lúc, tiết kiệm thời gian và công sức đáng kể.',
    icon: '📑',
  },
  {
    title: 'High-speed conversion',
    desc: 'Công nghệ xử lý tốc độ cao, chuyển đổi file chỉ trong vòng vài giây.',
    icon: '🚀',
  },
  {
    title: 'Cross-platform',
    desc: 'Hỗ trợ đầy đủ trên Windows, macOS, Linux, Android, iOS và Web.',
    icon: '💻',
  },
]

export default function Features() {
  return (
    <section className="features" id="features">
      <div className="container">
        <div className="section-header">
          <h2>Tính năng nổi bật</h2>
          <p>PDF PRO mang đến những tính năng mạnh mẽ giúp bạn làm việc hiệu quả hơn</p>
        </div>
        <div className="features-grid">
          {features.map((f) => (
            <div key={f.title} className="feature-card">
              <span className="feature-icon">{f.icon}</span>
              <h3>{f.title}</h3>
              <p>{f.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
