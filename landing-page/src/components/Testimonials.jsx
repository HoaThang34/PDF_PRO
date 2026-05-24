const testimonials = [
  {
    name: 'Nguyễn Hoàng Anh', role: 'Software Engineer', company: 'FPT Software',
    text: 'PDF PRO đã thay đổi cách tôi làm việc với PDF. Công cụ OCR cực kỳ chính xác, giúp tôi tiết kiệm hàng giờ đồng hồ mỗi tuần.',
    avatar: 'N',
  },
  {
    name: 'Trần Minh Quân', role: 'Product Manager', company: 'VNG Corp',
    text: 'Tính năng team workspace thực sự tuyệt vời. Cả team có thể cùng làm việc trên một file PDF một cách dễ dàng.',
    avatar: 'T',
  },
  {
    name: 'Lê Thị Hương', role: 'Giáo viên', company: 'Đại học Quốc gia',
    text: 'Tôi dùng PDF PRO để soạn giáo án và chấm bài. Giao diện thân thiện, dễ sử dụng. Hoàn toàn miễn phí cho giáo viên!',
    avatar: 'L',
  },
  {
    name: 'Phạm Đức Minh', role: 'Founder', company: 'Startup ABC',
    text: 'API của PDF PRO rất mạnh mẽ, giúp chúng tôi tích hợp xử lý PDF tự động vào hệ thống một cách nhanh chóng.',
    avatar: 'P',
  },
]

export default function Testimonials() {
  return (
    <section className="testimonials">
      <div className="container">
        <div className="section-header">
          <h2>Khách hàng nói gì</h2>
          <p>Hàng ngàn người dùng đã tin tưởng và sử dụng PDF PRO</p>
        </div>
        <div className="testimonials-grid">
          {testimonials.map((t, i) => (
            <div key={i} className="testimonial-card">
              <div className="testimonial-stars">★★★★★</div>
              <p className="testimonial-text">"{t.text}"</p>
              <div className="testimonial-author">
                <div className="testimonial-avatar">{t.avatar}</div>
                <div>
                  <div className="testimonial-name">{t.name}</div>
                  <div className="testimonial-role">{t.role} - {t.company}</div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}
