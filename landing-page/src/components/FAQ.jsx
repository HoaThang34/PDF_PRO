import { useState } from 'react'
import { IconChevronDown } from '../icons.jsx'

const faqs = [
  { q: 'PDF PRO có miễn phí không?', a: 'Có! PDF PRO hoàn toàn miễn phí với đầy đủ các tính năng cơ bản. Bạn có thể merge, split, nén và chuyển đổi PDF mà không mất bất kỳ khoản phí nào.' },
  { q: 'Có giới hạn dung lượng file không?', a: 'Ứng dụng hỗ trợ file dung lượng lên tới 2GB. Bạn có thể xử lý các file PDF lớn mà không lo bị gián đoạn.' },
  { q: 'File của tôi có bị lưu lại không?', a: 'File của bạn được tự động xóa khỏi server sau 24 giờ. Chúng tôi cam kết không đọc, lưu trữ hoặc chia sẻ dữ liệu của bạn với bất kỳ bên thứ ba nào.' },
  { q: 'PDF PRO có hỗ trợ OCR không?', a: 'Có! Tính năng OCR AI giúp nhận dạng văn bản từ hình ảnh scan với độ chính xác cao, hỗ trợ đa ngôn ngữ bao gồm tiếng Việt.' },
  { q: 'Có API để tích hợp không?', a: 'Có! PDF PRO cung cấp API đầy đủ cho phép bạn tích hợp xử lý PDF vào ứng dụng của mình.' },
  { q: 'Ứng dụng chạy trên những nền tảng nào?', a: 'Hiện tại PDF PRO hỗ trợ Windows 10/11 (64-bit). Phiên bản macOS, Linux và Web App đang được phát triển.' },
]

function FAQItem({ faq, open, onClick }) {
  return (
    <div className={`faq-item ${open ? 'faq-item--open' : ''}`}>
      <button className="faq-question" onClick={onClick}>
        <span>{faq.q}</span>
        <span className={`faq-arrow ${open ? 'faq-arrow--open' : ''}`}><IconChevronDown /></span>
      </button>
      <div className="faq-answer" style={{ maxHeight: open ? 200 : 0 }}>
        <p>{faq.a}</p>
      </div>
    </div>
  )
}

export default function FAQ() {
  const [openIndex, setOpenIndex] = useState(null)

  return (
    <section className="faq" id="faq">
      <div className="container">
        <div className="section-header">
          <h2>Câu hỏi thường gặp</h2>
          <p>Giải đáp mọi thắc mắc về PDF PRO</p>
        </div>
        <div className="faq-list">
          {faqs.map((faq, i) => (
            <FAQItem
              key={i}
              faq={faq}
              open={openIndex === i}
              onClick={() => setOpenIndex(openIndex === i ? null : i)}
            />
          ))}
        </div>
      </div>
    </section>
  )
}
