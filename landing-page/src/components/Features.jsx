import { IconAi, IconCloud, IconLightning, IconBatch, IconRocket, IconDevices } from '../icons.jsx'

const features = [
  {
    title: 'AI-powered tools',
    desc: 'Ứng dụng trí tuệ nhân tạo để nhận dạng văn bản, tối ưu hình ảnh và xử lý PDF thông minh, giúp tự động hóa các tác vụ phức tạp.',
    icon: IconAi,
  },
  {
    title: 'Cloud sync',
    desc: 'Đồng bộ dữ liệu lên đám mây, truy cập mọi lúc mọi nơi trên mọi thiết bị, đồng bộ hóa tiến độ làm việc liền mạch.',
    icon: IconCloud,
  },
  {
    title: 'Real-time editing',
    desc: 'Chỉnh sửa PDF trực tiếp trong thời gian thực, mọi thay đổi được hiển thị ngay lập tức trên giao diện trực quan.',
    icon: IconLightning,
  },
  {
    title: 'Batch processing',
    desc: 'Xử lý hàng loạt file cùng lúc với tốc độ cao, tiết kiệm thời gian và công sức khi làm việc với số lượng lớn tài liệu.',
    icon: IconBatch,
  },
  {
    title: 'High-speed conversion',
    desc: 'Công nghệ xử lý tốc độ cao, chuyển đổi và xử lý file chỉ trong vòng vài giây nhờ thuật toán tối ưu.',
    icon: IconRocket,
  },
  {
    title: 'Cross-platform',
    desc: 'Hỗ trợ đầy đủ trên Windows, macOS, Linux, Android, iOS và Web. Dù bạn ở đâu, PDF PRO luôn sẵn sàng phục vụ.',
    icon: IconDevices,
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
              <span className="feature-icon"><f.icon /></span>
              <h3>{f.title}</h3>
              <p>{f.desc}</p>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
